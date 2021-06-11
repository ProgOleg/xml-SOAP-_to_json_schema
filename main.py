import re
import json
import collections

import xmltodict
import genson
import jsonschema
import pyperclip


wsdl = """


"""


def camel_case_to_snake_case(string: str) -> str:
    return re.sub('([A-Z]+)', r'_\1', string).lower()


def parse_key(key: str):
    if len(key.split(':')) > 1:
        return key.split(':')[1]
    return key


def parse_body(obj):
    try:
        return obj.get('soapenv:Envelope').get('soapenv:Body')
    except AttributeError:
        return obj.get("soap:Envelope").get("soap:Body")


def type_handler(val, key):
    # key only for test purpose
    if isinstance(val, list):
        raise ValueError("LIST")
    if val in ['false', 'true', 'True', 'False']:
        return True
    try:
        val = int(val)
    except (ValueError, TypeError):
        pass
    else:
        return val
    try:
        val = float(val)
    except (ValueError, TypeError):
        pass
    else:
        return val
    if not isinstance(val, str):
        # 'typ1:nested' -> None todo: How to fix it?
        # raise ValueError("is something wrong, NO STR")
        return "is something wrong"
    return val


def main_handler(obj):
    for key in obj.keys():
        val = obj.get(key)
        if isinstance(val, collections.OrderedDict):
            main_handler(val)
        else:
            obj[key] = type_handler(val, key)


def key_handler(obj):
    a = {}
    for key, val in obj.items():
        cor_key = parse_key(key)
        if isinstance(val, collections.OrderedDict):
            temp_ = key_handler(val)
            a.update({cor_key: temp_})
        else:
            a.update({cor_key: val})
    return a


def main(xml_schema: str, test_data_only: bool = False):

    wsdl_dict = xmltodict.parse(xml_schema)
    body = dict(parse_body(wsdl_dict))
    main_handler(body)
    correct_body = key_handler(body)
    if not test_data_only:
        builder = genson.SchemaBuilder()
        builder.add_object(correct_body)
        schema = builder.to_schema()
        jsonschema.validate(instance=correct_body, schema=schema)
        return schema
    return correct_body


if __name__ == '__main__':
    # next string copy text from yor clipboard
    output = main(pyperclip.paste())

    # If this behavior is undesirable, uncomment the row below
    # output = main(wsdl)

    print(json.dumps(output, indent=4, sort_keys=True))
    # print("*" * 100)
    # print(camel_case_to_snake_case(list(output.keys())[0]), end="\n")

    # text to be copied to the clipboard!!!
    pyperclip.copy(json.dumps(output, indent=4, sort_keys=True))
