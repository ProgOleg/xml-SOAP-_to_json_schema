# xml_to_json_schema
Converts XML ( SOAP,  request example from SoapUI) to JSON schema and json example.

*XML*

    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Header>
        <ResponseHeader xmlns="https://www.google.com/apis/ads/publisher/v202105">
          <requestId>xxxxxxxxxxxxxxxxxxxx</requestId>
          <responseTime>1063</responseTime>
        </ResponseHeader>
      </soap:Header>
      <soap:Body>
        <getAdUnitsByStatementResponse xmlns="https://www.google.com/apis/ads/publisher/v202105">
          <rval>
            <totalResultSetSize>1</totalResultSetSize>
            <startIndex>0</startIndex>
            <results>
              <id>2372</id>
              <name>RootAdUnit</name>
              <description></description>
              <targetWindow>TOP</targetWindow>
              <status>ACTIVE</status>
              <adUnitCode>1002372</adUnitCode>
              <inheritedAdSenseSettings>
                <value>
                  <adSenseEnabled>true</adSenseEnabled>
                  <borderColor>FFFFFF</borderColor>
                  <titleColor>0000FF</titleColor>
                  <backgroundColor>FFFFFF</backgroundColor>
                  <textColor>000000</textColor>
                  <urlColor>008000</urlColor>
                  <adType>TEXT_AND_IMAGE</adType>
                  <borderStyle>DEFAULT</borderStyle>
                  <fontFamily>DEFAULT</fontFamily>
                  <fontSize>DEFAULT</fontSize>
                </value>
              </inheritedAdSenseSettings>
            </results>
          </rval>
        </getAdUnitsByStatementResponse>
      </soap:Body>
    </soap:Envelope>

*JSON chema*


    {
        "$schema": "http://json-schema.org/schema#",
        "properties": {
            "getAdUnitsByStatementResponse": {
                "properties": {
                    "@xmlns": {
                        "type": "string"
                    },
                    "rval": {
                        "properties": {
                            "results": {
                                "properties": {
                                    "adUnitCode": {
                                        "type": "integer"
                                    },
                                    "description": {
                                        "type": "string"
                                    },
                                    "id": {
                                        "type": "integer"
                                    },
                                    "inheritedAdSenseSettings": {
                                        "properties": {
                                            "value": {
                                                "properties": {
                                                    "adSenseEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "adType": {
                                                        "type": "string"
                                                    },
                                                    "backgroundColor": {
                                                        "type": "string"
                                                    },
                                                    "borderColor": {
                                                        "type": "string"
                                                    },
                                                    "borderStyle": {
                                                        "type": "string"
                                                    },
                                                    "fontFamily": {
                                                        "type": "string"
                                                    },
                                                    "fontSize": {
                                                        "type": "string"
                                                    },
                                                    "textColor": {
                                                        "type": "integer"
                                                    },
                                                    "titleColor": {
                                                        "type": "string"
                                                    },
                                                    "urlColor": {
                                                        "type": "integer"
                                                    }
                                                },
                                                "required": [
                                                    "adSenseEnabled",
                                                    "adType",
                                                    "backgroundColor",
                                                    "borderColor",
                                                    "borderStyle",
                                                    "fontFamily",
                                                    "fontSize",
                                                    "textColor",
                                                    "titleColor",
                                                    "urlColor"
                                                ],
                                                "type": "object"
                                            }
                                        },
                                        "required": [
                                            "value"
                                        ],
                                        "type": "object"
                                    },
                                    "name": {
                                        "type": "string"
                                    },
                                    "status": {
                                        "type": "string"
                                    },
                                    "targetWindow": {
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "adUnitCode",
                                    "description",
                                    "id",
                                    "inheritedAdSenseSettings",
                                    "name",
                                    "status",
                                    "targetWindow"
                                ],
                                "type": "object"
                            },
                            "startIndex": {
                                "type": "integer"
                            },
                            "totalResultSetSize": {
                                "type": "integer"
                            }
                        },
                        "required": [
                            "results",
                            "startIndex",
                            "totalResultSetSize"
                        ],
                        "type": "object"
                    }
                },
                "required": [
                    "@xmlns",
                    "rval"
                ],
                "type": "object"
            }
        },
        "required": [
            "getAdUnitsByStatementResponse"
        ],
        "type": "object"
    }

   
    
*JSON data example*


     {
            "getAdUnitsByStatementResponse": {
                "@xmlns": "https://www.google.com/apis/ads/publisher/v202105",
                "rval": {
                    "results": {
                        "adUnitCode": 1002372,
                        "description": "is something wrong",
                        "id": 2372,
                        "inheritedAdSenseSettings": {
                            "value": {
                                "adSenseEnabled": true,
                                "adType": "TEXT_AND_IMAGE",
                                "backgroundColor": "FFFFFF",
                                "borderColor": "FFFFFF",
                                "borderStyle": "DEFAULT",
                                "fontFamily": "DEFAULT",
                                "fontSize": "DEFAULT",
                                "textColor": 0,
                                "titleColor": "0000FF",
                                "urlColor": 8000
                            }
                        },
                        "name": "RootAdUnit",
                        "status": "ACTIVE",
                        "targetWindow": "TOP"
                    },
                    "startIndex": 0,
                    "totalResultSetSize": 1
                }
            }
        }
