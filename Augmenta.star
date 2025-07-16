{
  "metaData": {
    "version": "1.5.0b6",
    "versionNumber": 66816
  },
  "projectSettings": {
    "parameters": [
      {
        "value": true,
        "controlAddress": "/saveLayoutInFile"
      }
    ],
    "containers": {
      "dashboardSettings": {
        "parameters": [
          {
            "value": "",
            "controlAddress": "/showDashboardOnStartup",
            "enabled": false
          }
        ]
      },
      "customDefinitions": {
      },
      "nodeSettings": {
        "parameters": [
          {
            "value": "Kill App",
            "controlAddress": "/actionOnNodeCrash"
          }
        ]
      }
    }
  },
  "dashboardManager": {
    "viewOffset": [
      0,
      0
    ],
    "viewZoom": 1.0
  },
  "parrots": {
    "viewOffset": [
      0,
      0
    ],
    "viewZoom": 1.0
  },
  "layout": {
    "mainLayout": {
      "type": 1,
      "width": 1920,
      "height": 997,
      "direction": 2,
      "shifters": [
        {
          "type": 1,
          "width": 1920,
          "height": 997,
          "direction": 1,
          "shifters": [
            {
              "type": 1,
              "width": 470,
              "height": 997,
              "direction": 2,
              "shifters": [
                {
                  "type": 1,
                  "width": 470,
                  "height": 260,
                  "direction": 1,
                  "shifters": [
                    {
                      "type": 0,
                      "width": 307,
                      "height": 260,
                      "currentContent": "Outputs",
                      "tabs": [
                        {
                          "name": "Outputs"
                        }
                      ]
                    },
                    {
                      "type": 0,
                      "width": 157,
                      "height": 260,
                      "currentContent": "Sources",
                      "tabs": [
                        {
                          "name": "Sources"
                        }
                      ]
                    }
                  ]
                },
                {
                  "type": 0,
                  "width": 470,
                  "height": 201,
                  "currentContent": "Hierarchy",
                  "tabs": [
                    {
                      "name": "Hierarchy"
                    }
                  ]
                },
                {
                  "type": 0,
                  "width": 470,
                  "height": 315,
                  "currentContent": "Logger",
                  "tabs": [
                    {
                      "name": "Logger"
                    }
                  ]
                },
                {
                  "type": 0,
                  "width": 470,
                  "height": 201,
                  "tabs": null
                }
              ]
            },
            {
              "type": 1,
              "width": 760,
              "height": 997,
              "direction": 2,
              "shifters": [
                {
                  "type": 0,
                  "width": 760,
                  "height": 68,
                  "currentContent": "Worlds",
                  "tabs": [
                    {
                      "name": "Worlds"
                    }
                  ]
                },
                {
                  "type": 0,
                  "width": 760,
                  "height": 923,
                  "currentContent": "Node View",
                  "tabs": [
                    {
                      "name": "Node View"
                    }
                  ]
                }
              ]
            },
            {
              "type": 0,
              "width": 676,
              "height": 997,
              "currentContent": "Inspector",
              "tabs": [
                {
                  "name": "Inspector"
                }
              ]
            }
          ]
        }
      ]
    },
    "windows": null
  },
  "worlds": {
    "items": [
      {
        "niceName": "World",
        "containers": {
          "sources": {
            "items": [
              {
                "parameters": [
                  {
                    "value": false,
                    "controlAddress": "/enabled"
                  },
                  {
                    "value": true,
                    "controlAddress": "/processDepth"
                  },
                  {
                    "value": true,
                    "controlAddress": "/processColor"
                  },
                  {
                    "value": 3,
                    "hexMode": false,
                    "controlAddress": "/downSample"
                  },
                  {
                    "value": true,
                    "controlAddress": "/debugLog"
                  },
                  {
                    "value": "192.168.11.6",
                    "controlAddress": "/ip"
                  },
                  {
                    "value": "320x288",
                    "controlAddress": "/depthResolution"
                  },
                  {
                    "value": false,
                    "controlAddress": "/logCallbacksFrequency"
                  }
                ],
                "niceName": "cour",
                "type": "OrbbecNetwork",
                "lastDepthResolution": [
                  "320x288",
                  320
                ]
              },
              {
                "parameters": [
                  {
                    "value": false,
                    "controlAddress": "/enabled"
                  },
                  {
                    "value": 3,
                    "hexMode": false,
                    "controlAddress": "/downSample"
                  },
                  {
                    "value": "192.168.11.10",
                    "controlAddress": "/ip"
                  },
                  {
                    "value": "320x288",
                    "controlAddress": "/depthResolution"
                  }
                ],
                "niceName": "mid",
                "type": "OrbbecNetwork",
                "lastDepthResolution": [
                  "320x288",
                  320
                ]
              },
              {
                "parameters": [
                  {
                    "value": false,
                    "controlAddress": "/enabled"
                  },
                  {
                    "value": 3,
                    "hexMode": false,
                    "controlAddress": "/downSample"
                  },
                  {
                    "value": "192.168.11.14",
                    "controlAddress": "/ip"
                  },
                  {
                    "value": "320x288",
                    "controlAddress": "/depthResolution"
                  }
                ],
                "niceName": "ardin",
                "type": "OrbbecNetwork",
                "lastDepthResolution": [
                  "320x288",
                  320
                ]
              },
              {
                "parameters": [
                  {
                    "value": false,
                    "controlAddress": "/enabled"
                  },
                  {
                    "value": 3,
                    "hexMode": false,
                    "controlAddress": "/downSample"
                  },
                  {
                    "value": "192.168.11.2",
                    "controlAddress": "/ip"
                  },
                  {
                    "value": "320x288",
                    "controlAddress": "/depthResolution"
                  }
                ],
                "niceName": "Front",
                "type": "OrbbecNetwork",
                "lastDepthResolution": [
                  "320x288",
                  320
                ]
              }
            ],
            "viewOffset": [
              0,
              0
            ],
            "viewZoom": 1.0
          },
          "outputs": {
            "hideInEditor": true,
            "items": [
              {
                "parameters": [
                  {
                    "value": true,
                    "controlAddress": "/enabled"
                  },
                  {
                    "value": false,
                    "controlAddress": "/autoRegisterClients"
                  },
                  {
                    "value": true,
                    "controlAddress": "/updateClientOnRegister"
                  },
                  {
                    "value": 12,
                    "hexMode": false,
                    "controlAddress": "/downsample"
                  },
                  {
                    "value": true,
                    "controlAddress": "/streamClouds"
                  },
                  {
                    "value": true,
                    "controlAddress": "/streamClusters"
                  },
                  {
                    "value": true,
                    "controlAddress": "/streamClusterPoints"
                  }
                ],
                "niceName": "Websocket",
                "containers": {
                  "tags": {
                    "viewOffset": [
                      0,
                      0
                    ],
                    "viewZoom": 1.0
                  },
                  "axisTransform": {
                    "parameters": [
                      {
                        "value": true,
                        "controlAddress": "/enabled"
                      },
                      {
                        "value": "Absolute",
                        "controlAddress": "/coordinateSpace"
                      },
                      {
                        "value": "Custom ...",
                        "controlAddress": "/coordinateSystem"
                      },
                      {
                        "value": [
                          0.0,
                          0.0,
                          0.0
                        ],
                        "controlAddress": "/originOffset"
                      },
                      {
                        "value": false,
                        "controlAddress": "/flipXAxis"
                      },
                      {
                        "value": false,
                        "controlAddress": "/flipYAxis"
                      },
                      {
                        "value": false,
                        "controlAddress": "/flipZAxis"
                      },
                      {
                        "value": [
                          1.0,
                          0.0,
                          0.0
                        ],
                        "controlAddress": "/x__"
                      },
                      {
                        "value": [
                          0.0,
                          1.0,
                          0.0
                        ],
                        "controlAddress": "/y__"
                      },
                      {
                        "value": [
                          0.0,
                          0.0,
                          1.0
                        ],
                        "controlAddress": "/z__"
                      }
                    ]
                  },
                  "clients": {
                  }
                },
                "type": "Websocket"
              },
              {
                "parameters": [
                  {
                    "value": 3335,
                    "hexMode": false,
                    "controlAddress": "/port"
                  }
                ],
                "niceName": "OSC Python",
                "containers": {
                  "tags": {
                    "viewOffset": [
                      0,
                      0
                    ],
                    "viewZoom": 1.0
                  },
                  "axisTransform": {
                    "parameters": [
                      {
                        "value": false,
                        "controlAddress": "/enabled"
                      },
                      {
                        "value": "Relative",
                        "controlAddress": "/coordinateSpace"
                      },
                      {
                        "value": [
                          1.0,
                          0.0,
                          0.0
                        ],
                        "controlAddress": "/x__"
                      },
                      {
                        "value": [
                          0.0,
                          1.0,
                          0.0
                        ],
                        "controlAddress": "/y__"
                      },
                      {
                        "value": [
                          0.0,
                          0.0,
                          1.0
                        ],
                        "controlAddress": "/z__"
                      }
                    ],
                    "editorIsCollapsed": true
                  },
                  "oscParameters": {
                    "parameters": [
                      {
                        "value": false,
                        "controlAddress": "/splitCoordinates"
                      },
                      {
                        "value": "/highest/pos",
                        "controlAddress": "/sendHeight",
                        "enabled": false
                      },
                      {
                        "value": "/speed/dir",
                        "controlAddress": "/sendSpeed",
                        "enabled": false
                      },
                      {
                        "value": "/speed/val",
                        "controlAddress": "/sendSpeedNorm",
                        "enabled": false
                      },
                      {
                        "value": "/box/{type}",
                        "controlAddress": "/sendBoundingBox",
                        "enabled": false
                      },
                      {
                        "value": "/age",
                        "controlAddress": "/sendAge",
                        "enabled": true
                      }
                    ]
                  }
                },
                "type": "Augmenta V3"
              }
            ],
            "viewOffset": [
              0,
              0
            ],
            "viewZoom": 1.0
          },
          "children": {
            "hideInEditor": true,
            "items": [
              {
                "parameters": [
                  {
                    "value": true,
                    "controlAddress": "/locked"
                  },
                  {
                    "value": [
                      0.8666666746139526,
                      0.8666666746139526,
                      0.8666666746139526,
                      1.0
                    ],
                    "controlAddress": "/color"
                  },
                  {
                    "value": [
                      7.301569127093899e-8,
                      0.0,
                      0.01056450232863426
                    ],
                    "controlAddress": "/position"
                  },
                  {
                    "value": [
                      13.07999992370605,
                      7.0,
                      9.770000457763672
                    ],
                    "controlAddress": "/size"
                  }
                ],
                "niceName": "Scene",
                "containers": {
                  "children": {
                    "hideInEditor": true,
                    "items": [
                      {
                        "parameters": [
                          {
                            "value": true,
                            "controlAddress": "/locked"
                          },
                          {
                            "value": [
                              0.8666666746139526,
                              0.8666666746139526,
                              0.8666666746139526,
                              1.0
                            ],
                            "controlAddress": "/color"
                          },
                          {
                            "value": [
                              -0.2150000035762787,
                              0.0,
                              0.4799999892711639
                            ],
                            "controlAddress": "/position"
                          },
                          {
                            "value": [
                              0.0,
                              1.200000166893005,
                              0.0
                            ],
                            "controlAddress": "/rotation"
                          }
                        ],
                        "niceName": "Camera Setup",
                        "containers": {
                          "tags": {
                            "viewOffset": [
                              0,
                              0
                            ],
                            "viewZoom": 1.0
                          },
                          "children": {
                            "hideInEditor": true,
                            "items": [
                              {
                                "parameters": [
                                  {
                                    "value": [
                                      0.6980392336845398,
                                      0.3490196168422699,
                                      0.3490196168422699,
                                      1.0
                                    ],
                                    "controlAddress": "/color"
                                  },
                                  {
                                    "value": [
                                      9.836130142211914,
                                      0.0,
                                      4.292399406433105
                                    ],
                                    "controlAddress": "/position"
                                  },
                                  {
                                    "value": [
                                      180.0,
                                      -87.38124084472656,
                                      179.8262023925781
                                    ],
                                    "controlAddress": "/rotation"
                                  },
                                  {
                                    "value": "/cour",
                                    "controlAddress": "/source"
                                  }
                                ],
                                "niceName": "cour",
                                "containers": {
                                  "tags": {
                                    "viewOffset": [
                                      0,
                                      0
                                    ],
                                    "viewZoom": 1.0
                                  },
                                  "children": {
                                    "hideInEditor": true,
                                    "viewOffset": [
                                      0,
                                      0
                                    ],
                                    "viewZoom": 1.0
                                  },
                                  "axisTransform": {
                                    "parameters": [
                                      {
                                        "value": false,
                                        "controlAddress": "/enabled"
                                      },
                                      {
                                        "value": [
                                          1.0,
                                          0.0,
                                          0.0
                                        ],
                                        "controlAddress": "/x__"
                                      },
                                      {
                                        "value": [
                                          0.0,
                                          1.0,
                                          0.0
                                        ],
                                        "controlAddress": "/y__"
                                      },
                                      {
                                        "value": [
                                          0.0,
                                          0.0,
                                          1.0
                                        ],
                                        "controlAddress": "/z__"
                                      }
                                    ],
                                    "editorIsCollapsed": true
                                  },
                                  "physicalCamera": {
                                    "parameters": [
                                      {
                                        "value": [
                                          0.2285283505916595,
                                          7.389559745788574,
                                          0.2313640713691711
                                        ],
                                        "controlAddress": "/position"
                                      },
                                      {
                                        "value": [
                                          104.7956695556641,
                                          -0.8058596253395081,
                                          0.6206480264663696
                                        ],
                                        "controlAddress": "/rotation"
                                      }
                                    ]
                                  }
                                },
                                "type": "Camera"
                              },
                              {
                                "parameters": [
                                  {
                                    "value": false,
                                    "controlAddress": "/locked"
                                  },
                                  {
                                    "value": [
                                      0.3490196168422699,
                                      0.7019608020782471,
                                      0.3803921639919281,
                                      1.0
                                    ],
                                    "controlAddress": "/color"
                                  },
                                  {
                                    "value": [
                                      6.705965995788574,
                                      0.0,
                                      4.255835056304932
                                    ],
                                    "controlAddress": "/position"
                                  },
                                  {
                                    "value": [
                                      -8.678281482104797e-14,
                                      -85.71270751953125,
                                      7.225907968765738e-14
                                    ],
                                    "controlAddress": "/rotation"
                                  },
                                  {
                                    "value": "/mid",
                                    "controlAddress": "/source"
                                  }
                                ],
                                "niceName": "mid",
                                "containers": {
                                  "tags": {
                                    "viewOffset": [
                                      0,
                                      0
                                    ],
                                    "viewZoom": 1.0
                                  },
                                  "children": {
                                    "hideInEditor": true,
                                    "viewOffset": [
                                      0,
                                      0
                                    ],
                                    "viewZoom": 1.0
                                  },
                                  "axisTransform": {
                                    "parameters": [
                                      {
                                        "value": false,
                                        "controlAddress": "/enabled"
                                      },
                                      {
                                        "value": "Relative",
                                        "controlAddress": "/coordinateSpace"
                                      },
                                      {
                                        "value": [
                                          -1.499999761581421,
                                          0.0,
                                          -1.999998092651367
                                        ],
                                        "controlAddress": "/originOffset"
                                      },
                                      {
                                        "value": [
                                          1.0,
                                          0.0,
                                          0.0
                                        ],
                                        "controlAddress": "/x__"
                                      },
                                      {
                                        "value": [
                                          0.0,
                                          1.0,
                                          0.0
                                        ],
                                        "controlAddress": "/y__"
                                      },
                                      {
                                        "value": [
                                          0.0,
                                          0.0,
                                          1.0
                                        ],
                                        "controlAddress": "/z__"
                                      }
                                    ],
                                    "editorIsCollapsed": true
                                  },
                                  "physicalCamera": {
                                    "parameters": [
                                      {
                                        "value": [
                                          0.1661447584629059,
                                          7.360490322113037,
                                          0.1924244910478592
                                        ],
                                        "controlAddress": "/position"
                                      },
                                      {
                                        "value": [
                                          94.49767303466797,
                                          -1.925078272819519,
                                          1.779621005058289
                                        ],
                                        "controlAddress": "/rotation"
                                      }
                                    ]
                                  }
                                },
                                "type": "Camera"
                              },
                              {
                                "parameters": [
                                  {
                                    "value": [
                                      0.3490196168422699,
                                      0.3607843220233917,
                                      0.7019608020782471,
                                      1.0
                                    ],
                                    "controlAddress": "/color"
                                  },
                                  {
                                    "value": [
                                      2.727616310119629,
                                      0.0,
                                      3.912527084350586
                                    ],
                                    "controlAddress": "/position"
                                  },
                                  {
                                    "value": [
                                      0.0,
                                      -86.10735321044922,
                                      0.0
                                    ],
                                    "controlAddress": "/rotation"
                                  },
                                  {
                                    "value": "/ardin",
                                    "controlAddress": "/source"
                                  }
                                ],
                                "niceName": "ardin",
                                "containers": {
                                  "tags": {
                                    "viewOffset": [
                                      0,
                                      0
                                    ],
                                    "viewZoom": 1.0
                                  },
                                  "children": {
                                    "hideInEditor": true,
                                    "viewOffset": [
                                      0,
                                      0
                                    ],
                                    "viewZoom": 1.0
                                  },
                                  "axisTransform": {
                                    "parameters": [
                                      {
                                        "value": false,
                                        "controlAddress": "/enabled"
                                      },
                                      {
                                        "value": [
                                          -0.3999999463558197,
                                          0.0,
                                          -2.699999809265137
                                        ],
                                        "controlAddress": "/originOffset"
                                      },
                                      {
                                        "value": [
                                          1.0,
                                          0.0,
                                          0.0
                                        ],
                                        "controlAddress": "/x__"
                                      },
                                      {
                                        "value": [
                                          0.0,
                                          1.0,
                                          0.0
                                        ],
                                        "controlAddress": "/y__"
                                      },
                                      {
                                        "value": [
                                          0.0,
                                          0.0,
                                          1.0
                                        ],
                                        "controlAddress": "/z__"
                                      }
                                    ],
                                    "editorIsCollapsed": true
                                  },
                                  "physicalCamera": {
                                    "parameters": [
                                      {
                                        "value": [
                                          0.5428898930549622,
                                          7.421589851379395,
                                          -0.6730388402938843
                                        ],
                                        "controlAddress": "/position"
                                      },
                                      {
                                        "value": [
                                          85.22187805175781,
                                          -1.685316801071167,
                                          1.832041025161743
                                        ],
                                        "controlAddress": "/rotation"
                                      }
                                    ]
                                  }
                                },
                                "type": "Camera"
                              },
                              {
                                "parameters": [
                                  {
                                    "value": [
                                      1.0,
                                      1.0,
                                      1.0,
                                      1.0
                                    ],
                                    "controlAddress": "/color"
                                  },
                                  {
                                    "value": [
                                      7.036207675933838,
                                      -8.881784197001252e-15,
                                      1.681406736373901
                                    ],
                                    "controlAddress": "/position"
                                  },
                                  {
                                    "value": [
                                      0.0,
                                      0.0,
                                      0.0
                                    ],
                                    "controlAddress": "/rotation"
                                  },
                                  {
                                    "value": "/front",
                                    "controlAddress": "/source"
                                  }
                                ],
                                "niceName": "Front",
                                "containers": {
                                  "tags": {
                                    "viewOffset": [
                                      0,
                                      0
                                    ],
                                    "viewZoom": 1.0
                                  },
                                  "children": {
                                    "hideInEditor": true,
                                    "viewOffset": [
                                      0,
                                      0
                                    ],
                                    "viewZoom": 1.0
                                  },
                                  "axisTransform": {
                                    "parameters": [
                                      {
                                        "value": false,
                                        "controlAddress": "/enabled"
                                      },
                                      {
                                        "value": "Normalized",
                                        "controlAddress": "/coordinateSpace"
                                      },
                                      {
                                        "value": [
                                          0.0,
                                          0.0,
                                          0.0
                                        ],
                                        "controlAddress": "/originOffset"
                                      },
                                      {
                                        "value": false,
                                        "controlAddress": "/flipZAxis"
                                      },
                                      {
                                        "value": [
                                          1.0,
                                          0.0,
                                          0.0
                                        ],
                                        "controlAddress": "/x__"
                                      },
                                      {
                                        "value": [
                                          0.0,
                                          1.0,
                                          0.0
                                        ],
                                        "controlAddress": "/y__"
                                      },
                                      {
                                        "value": [
                                          0.0,
                                          0.0,
                                          1.0
                                        ],
                                        "controlAddress": "/z__"
                                      }
                                    ],
                                    "editorIsCollapsed": true
                                  },
                                  "physicalCamera": {
                                    "parameters": [
                                      {
                                        "value": [
                                          -0.3600451946258545,
                                          7.25577974319458,
                                          -3.233890295028687
                                        ],
                                        "controlAddress": "/position"
                                      },
                                      {
                                        "value": [
                                          56.7765998840332,
                                          -1.7027667760849,
                                          3.150177717208862
                                        ],
                                        "controlAddress": "/rotation"
                                      }
                                    ]
                                  }
                                },
                                "type": "Camera"
                              }
                            ],
                            "viewOffset": [
                              0,
                              0
                            ],
                            "viewZoom": 1.0
                          },
                          "axisTransform": {
                            "parameters": [
                              {
                                "value": false,
                                "controlAddress": "/enabled"
                              },
                              {
                                "value": [
                                  1.0,
                                  0.0,
                                  0.0
                                ],
                                "controlAddress": "/x__"
                              },
                              {
                                "value": [
                                  0.0,
                                  1.0,
                                  0.0
                                ],
                                "controlAddress": "/y__"
                              },
                              {
                                "value": [
                                  0.0,
                                  0.0,
                                  1.0
                                ],
                                "controlAddress": "/z__"
                              }
                            ],
                            "editorIsCollapsed": true
                          }
                        },
                        "type": "Camera Setup"
                      },
                      {
                        "parameters": [
                          {
                            "value": true,
                            "controlAddress": "/enabled"
                          },
                          {
                            "value": true,
                            "controlAddress": "/locked"
                          },
                          {
                            "value": [
                              0.8666666746139526,
                              0.8666666746139526,
                              0.8666666746139526,
                              1.0
                            ],
                            "controlAddress": "/color"
                          },
                          {
                            "value": [
                              0.0,
                              0.1000000014901161,
                              0.0
                            ],
                            "controlAddress": "/position"
                          },
                          {
                            "value": "Intersect",
                            "controlAddress": "/cropMode"
                          },
                          {
                            "value": false,
                            "controlAddress": "/cropData"
                          }
                        ],
                        "niceName": "Remove Floor",
                        "containers": {
                          "tags": {
                            "viewOffset": [
                              0,
                              0
                            ],
                            "viewZoom": 1.0
                          },
                          "children": {
                            "hideInEditor": true,
                            "viewOffset": [
                              0,
                              0
                            ],
                            "viewZoom": 1.0
                          },
                          "axisTransform": {
                            "parameters": [
                              {
                                "value": false,
                                "controlAddress": "/enabled"
                              },
                              {
                                "value": [
                                  1.0,
                                  0.0,
                                  0.0
                                ],
                                "controlAddress": "/x__"
                              },
                              {
                                "value": [
                                  0.0,
                                  1.0,
                                  0.0
                                ],
                                "controlAddress": "/y__"
                              },
                              {
                                "value": [
                                  0.0,
                                  0.0,
                                  1.0
                                ],
                                "controlAddress": "/z__"
                              }
                            ],
                            "editorIsCollapsed": true
                          },
                          "box": {
                            "parameters": [
                              {
                                "value": [
                                  13.10000038146973,
                                  5.5,
                                  8.399999618530273
                                ],
                                "controlAddress": "/boxSize"
                              }
                            ]
                          }
                        },
                        "type": "Crop"
                      }
                    ],
                    "viewOffset": [
                      0,
                      0
                    ],
                    "viewZoom": 1.0
                  },
                  "tag": {
                    "parameters": [
                      {
                        "value": "",
                        "controlAddress": "/tag"
                      }
                    ],
                    "niceName": "Tag",
                    "type": "Tag Selector"
                  },
                  "axisTransform": {
                    "parameters": [
                      {
                        "value": false,
                        "controlAddress": "/enabled"
                      },
                      {
                        "value": "Relative",
                        "controlAddress": "/coordinateSpace"
                      },
                      {
                        "value": [
                          0.0,
                          0.0,
                          0.0
                        ],
                        "controlAddress": "/originOffset"
                      },
                      {
                        "value": false,
                        "controlAddress": "/flipXAxis"
                      },
                      {
                        "value": [
                          1.0,
                          0.0,
                          0.0
                        ],
                        "controlAddress": "/x__"
                      },
                      {
                        "value": [
                          0.0,
                          1.0,
                          0.0
                        ],
                        "controlAddress": "/y__"
                      },
                      {
                        "value": [
                          0.0,
                          0.0,
                          1.0
                        ],
                        "controlAddress": "/z__"
                      }
                    ],
                    "editorIsCollapsed": true
                  },
                  "metaParameters": {
                    "items": [
                      {
                        "parameters": [
                          {
                            "value": false,
                            "minValue": 0,
                            "maxValue": 1,
                            "default": false,
                            "controlAddress": "/value",
                            "type": "Boolean",
                            "niceName": "Value",
                            "customizable": true,
                            "removable": false,
                            "description": "",
                            "hideInEditor": false,
                            "feedbackOnly": false
                          }
                        ],
                        "niceName": "SimulatorEnabled",
                        "editorIsCollapsed": true,
                        "containers": {
                          "mappings": {
                            "items": [
                              {
                                "parameters": [
                                  {
                                    "value": "/nodes/simulatorSource/enabled",
                                    "controlAddress": "/target"
                                  }
                                ],
                                "niceName": "Mapping",
                                "type": "Mapping"
                              },
                              {
                                "parameters": [
                                  {
                                    "value": "/nodes/appendClusters/waitForAllInputs",
                                    "controlAddress": "/target"
                                  }
                                ],
                                "niceName": "Mapping 1",
                                "type": "Mapping"
                              }
                            ],
                            "viewOffset": [
                              0,
                              0
                            ],
                            "viewZoom": 1.0
                          },
                          "scripts": {
                            "viewOffset": [
                              0,
                              0
                            ],
                            "viewZoom": 1.0
                          }
                        },
                        "type": "Boolean",
                        "scripts": {
                          "viewOffset": [
                            0,
                            0
                          ],
                          "viewZoom": 1.0
                        }
                      },
                      {
                        "parameters": [
                          {
                            "value": true,
                            "minValue": 0,
                            "maxValue": 1,
                            "default": false,
                            "controlAddress": "/value",
                            "type": "Boolean",
                            "niceName": "Value",
                            "customizable": true,
                            "removable": false,
                            "description": "",
                            "hideInEditor": false,
                            "feedbackOnly": false
                          }
                        ],
                        "niceName": "FilteredCloudOut",
                        "containers": {
                          "mappings": {
                            "items": [
                              {
                                "parameters": [
                                  {
                                    "value": "/nodes/cloudRecorder1/passthroughEnabled",
                                    "controlAddress": "/target"
                                  }
                                ],
                                "niceName": "Mapping",
                                "type": "Mapping"
                              }
                            ],
                            "viewOffset": [
                              0,
                              0
                            ],
                            "viewZoom": 1.0
                          },
                          "scripts": {
                            "viewOffset": [
                              0,
                              0
                            ],
                            "viewZoom": 1.0
                          }
                        },
                        "type": "Boolean",
                        "scripts": {
                          "viewOffset": [
                            0,
                            0
                          ],
                          "viewZoom": 1.0
                        }
                      },
                      {
                        "parameters": [
                          {
                            "value": false,
                            "controlAddress": "/enabled"
                          },
                          {
                            "value": true,
                            "minValue": 0,
                            "maxValue": 1,
                            "default": false,
                            "controlAddress": "/value",
                            "type": "Boolean",
                            "niceName": "Value",
                            "customizable": true,
                            "removable": false,
                            "description": "",
                            "hideInEditor": false,
                            "feedbackOnly": false
                          }
                        ],
                        "niceName": "OutState",
                        "editorIsCollapsed": true,
                        "containers": {
                          "mappings": {
                            "items": [
                              {
                                "parameters": [
                                  {
                                    "value": "/nodes/outFilter/enabled",
                                    "controlAddress": "/target"
                                  }
                                ],
                                "niceName": "Mapping",
                                "type": "Mapping"
                              },
                              {
                                "parameters": [
                                  {
                                    "value": "/nodes/outMerge/enabled",
                                    "controlAddress": "/target"
                                  }
                                ],
                                "niceName": "Mapping 1",
                                "type": "Mapping"
                              }
                            ],
                            "viewOffset": [
                              0,
                              0
                            ],
                            "viewZoom": 1.0
                          },
                          "scripts": {
                            "viewOffset": [
                              0,
                              0
                            ],
                            "viewZoom": 1.0
                          }
                        },
                        "type": "Boolean",
                        "scripts": {
                          "viewOffset": [
                            0,
                            0
                          ],
                          "viewZoom": 1.0
                        }
                      }
                    ],
                    "viewOffset": [
                      0,
                      0
                    ],
                    "viewZoom": 1.0
                  },
                  "nodes": {
                    "hideInEditor": true,
                    "items": [
                      {
                        "parameters": [
                          {
                            "value": false,
                            "controlAddress": "/miniMode"
                          },
                          {
                            "value": [
                              -1573.0,
                              -385.0
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              221.0,
                              76.0
                            ],
                            "controlAddress": "/viewUISize"
                          },
                          {
                            "value": "Before Merge",
                            "controlAddress": "/cropOrder"
                          }
                        ],
                        "niceName": "World Cameras",
                        "type": "World Cameras"
                      },
                      {
                        "parameters": [
                          {
                            "value": [
                              980.7058715820312,
                              -427.2941284179688
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              240.0,
                              80.0
                            ],
                            "controlAddress": "/viewUISize"
                          }
                        ],
                        "niceName": "Out default",
                        "containers": {
                          "tag": {
                            "parameters": [
                              {
                                "value": "",
                                "controlAddress": "/tag"
                              }
                            ],
                            "niceName": "Tag",
                            "type": "Tag Selector"
                          }
                        },
                        "type": "Out"
                      },
                      {
                        "parameters": [
                          {
                            "value": true,
                            "controlAddress": "/enabled"
                          },
                          {
                            "value": [
                              -119.7948684692383,
                              -262.5641174316406
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              240.0,
                              80.0
                            ],
                            "controlAddress": "/viewUISize"
                          },
                          {
                            "value": 0.113000000047497,
                            "controlAddress": "/tolerance"
                          },
                          {
                            "value": 0.017,
                            "controlAddress": "/preFilter",
                            "enabled": false
                          },
                          {
                            "value": 0.083,
                            "controlAddress": "/verticalCompression"
                          },
                          {
                            "value": 13,
                            "hexMode": false,
                            "controlAddress": "/minCount"
                          },
                          {
                            "value": 11069,
                            "hexMode": false,
                            "controlAddress": "/maxCount"
                          },
                          {
                            "value": [
                              2.0,
                              5.0,
                              2.0
                            ],
                            "controlAddress": "/maxSize"
                          },
                          {
                            "value": true,
                            "controlAddress": "/computeBox"
                          },
                          {
                            "value": true,
                            "controlAddress": "/extendToFloor"
                          }
                        ],
                        "niceName": "Euclidean Cluster",
                        "type": "Euclidean Cluster"
                      },
                      {
                        "parameters": [
                          {
                            "value": true,
                            "controlAddress": "/enabled"
                          },
                          {
                            "value": [
                              -1263.0,
                              -140.0
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              240.0,
                              80.0
                            ],
                            "controlAddress": "/viewUISize"
                          },
                          {
                            "value": 0.7319999933242798,
                            "controlAddress": "/searchDistance"
                          }
                        ],
                        "niceName": "Tracker",
                        "containers": {
                          "ghosting": {
                            "parameters": [
                              {
                                "value": false,
                                "controlAddress": "/enabled"
                              },
                              {
                                "value": 0.330254077911377,
                                "controlAddress": "/ghostSearchDistance"
                              },
                              {
                                "value": 0.0984090194106102,
                                "controlAddress": "/minGhostAge"
                              },
                              {
                                "value": 0.6205286383628845,
                                "controlAddress": "/maxGhostAge"
                              },
                              {
                                "value": 0.08016423881053925,
                                "controlAddress": "/ghostInertia"
                              }
                            ],
                            "editorIsCollapsed": true
                          },
                          "weighting": {
                            "parameters": [
                              {
                                "value": false,
                                "controlAddress": "/enabled"
                              }
                            ],
                            "editorIsCollapsed": true,
                            "containers": {
                              "weightCurve": {
                                "parameters": [
                                  {
                                    "value": 1.0,
                                    "controlAddress": "/length"
                                  },
                                  {
                                    "value": [
                                      0.0,
                                      1.0
                                    ],
                                    "controlAddress": "/viewValueRange"
                                  },
                                  {
                                    "value": [
                                      0.0,
                                      1.0
                                    ],
                                    "controlAddress": "/range",
                                    "enabled": true
                                  }
                                ],
                                "hideInRemoteControl": false,
                                "items": [
                                  {
                                    "parameters": [
                                      {
                                        "value": "Bezier",
                                        "controlAddress": "/easingType"
                                      }
                                    ],
                                    "niceName": "Key",
                                    "containers": {
                                      "easing": {
                                        "parameters": [
                                          {
                                            "value": [
                                              0.300000011920929,
                                              0.0
                                            ],
                                            "controlAddress": "/anchor1"
                                          },
                                          {
                                            "value": [
                                              -0.300000011920929,
                                              0.0
                                            ],
                                            "controlAddress": "/anchor2"
                                          }
                                        ]
                                      }
                                    },
                                    "type": "Key"
                                  },
                                  {
                                    "parameters": [
                                      {
                                        "value": 1.0,
                                        "controlAddress": "/position"
                                      },
                                      {
                                        "value": 1.0,
                                        "controlAddress": "/value"
                                      },
                                      {
                                        "value": "Bezier",
                                        "controlAddress": "/easingType"
                                      }
                                    ],
                                    "niceName": "Key 1",
                                    "containers": {
                                      "easing": {
                                      }
                                    },
                                    "type": "Key"
                                  }
                                ],
                                "viewOffset": [
                                  0,
                                  0
                                ],
                                "viewZoom": 1.0
                              }
                            }
                          }
                        },
                        "type": "Tracker"
                      },
                      {
                        "parameters": [
                          {
                            "value": true,
                            "controlAddress": "/enabled"
                          },
                          {
                            "value": [
                              -703.0,
                              -141.0
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              240.0,
                              80.0
                            ],
                            "controlAddress": "/viewUISize"
                          },
                          {
                            "value": false,
                            "controlAddress": "/log"
                          },
                          {
                            "value": 150,
                            "hexMode": false,
                            "controlAddress": "/maxSlots"
                          },
                          {
                            "value": false,
                            "controlAddress": "/strictMode"
                          }
                        ],
                        "niceName": "Slot",
                        "type": "Slot"
                      },
                      {
                        "parameters": [
                          {
                            "value": true,
                            "controlAddress": "/enabled"
                          },
                          {
                            "value": [
                              -405.0,
                              -141.0
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              240.0,
                              80.0
                            ],
                            "controlAddress": "/viewUISize"
                          }
                        ],
                        "niceName": "One Euro Filter",
                        "containers": {
                          "position": {
                            "parameters": [
                              {
                                "value": true,
                                "controlAddress": "/enabled"
                              },
                              {
                                "value": 0.699999988079071,
                                "controlAddress": "/minCutoff"
                              },
                              {
                                "value": 1.0,
                                "controlAddress": "/beta"
                              },
                              {
                                "value": 1.0,
                                "controlAddress": "/derivativeCutOff"
                              }
                            ]
                          },
                          "size": {
                            "editorIsCollapsed": true
                          },
                          "velocity": {
                            "parameters": [
                              {
                                "value": true,
                                "controlAddress": "/enabled"
                              },
                              {
                                "value": 0.3,
                                "controlAddress": "/minCutoff"
                              },
                              {
                                "value": 1.0,
                                "controlAddress": "/beta"
                              },
                              {
                                "value": 1.0,
                                "controlAddress": "/derivativeCutOff"
                              }
                            ]
                          },
                          "rotation": {
                            "editorIsCollapsed": true
                          }
                        },
                        "type": "One Euro Filter"
                      },
                      {
                        "parameters": [
                          {
                            "value": true,
                            "controlAddress": "/enabled"
                          },
                          {
                            "value": [
                              -119.0,
                              -141.0
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              240.0,
                              80.0
                            ],
                            "controlAddress": "/viewUISize"
                          },
                          {
                            "value": 13.28966903686523,
                            "controlAddress": "/strength"
                          },
                          {
                            "value": 0.4804555773735046,
                            "controlAddress": "/velocityTreshold"
                          }
                        ],
                        "niceName": "Prediction",
                        "type": "Prediction"
                      },
                      {
                        "parameters": [
                          {
                            "value": [
                              534.0,
                              -53.0
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              240.0,
                              80.0
                            ],
                            "controlAddress": "/viewUISize"
                          }
                        ],
                        "niceName": "Zone Process",
                        "type": "Zone Process"
                      },
                      {
                        "parameters": [
                          {
                            "value": [
                              -1258.756225585938,
                              -493.1380615234375
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              240.0,
                              80.0
                            ],
                            "controlAddress": "/viewUISize"
                          },
                          {
                            "value": "Merge",
                            "controlAddress": "/systemTag"
                          },
                          {
                            "value": true,
                            "controlAddress": "/sendToEditorOnly"
                          }
                        ],
                        "niceName": "Out merge",
                        "containers": {
                          "tag": {
                            "parameters": [
                              {
                                "value": "",
                                "controlAddress": "/tag"
                              }
                            ],
                            "niceName": "Tag",
                            "type": "Tag Selector"
                          }
                        },
                        "type": "Out"
                      },
                      {
                        "parameters": [
                          {
                            "value": false,
                            "controlAddress": "/enabled"
                          },
                          {
                            "value": [
                              -113.6326522827148,
                              -364.4081726074219
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              240.0,
                              80.0
                            ],
                            "controlAddress": "/viewUISize"
                          }
                        ],
                        "niceName": "SimulatorSource",
                        "editorIsCollapsed": true,
                        "containers": {
                          "behaviour": {
                            "parameters": [
                              {
                                "value": "Human in a museum",
                                "controlAddress": "/presets"
                              }
                            ]
                          },
                          "number": {
                            "parameters": [
                              {
                                "value": 4,
                                "hexMode": false,
                                "controlAddress": "/n"
                              }
                            ]
                          },
                          "orientation": {
                          },
                          "size": {
                            "parameters": [
                              {
                                "value": [
                                  0.2000000029802322,
                                  0.5,
                                  0.2000000029802322
                                ],
                                "controlAddress": "/min"
                              },
                              {
                                "value": [
                                  0.6000000238418579,
                                  2.0,
                                  0.6000000238418579
                                ],
                                "controlAddress": "/max"
                              },
                              {
                                "value": 0.3,
                                "controlAddress": "/sizeVariationSpeed",
                                "enabled": false
                              }
                            ]
                          },
                          "velocity": {
                            "parameters": [
                              {
                                "value": [
                                  0.0,
                                  1.0
                                ],
                                "controlAddress": "/min_Max"
                              },
                              {
                                "value": [
                                  0.25,
                                  0.300000011920929,
                                  0.25
                                ],
                                "controlAddress": "/marging"
                              },
                              {
                                "value": [
                                  0.05000000074505806,
                                  0.2000000029802322
                                ],
                                "controlAddress": "/displacementNoise",
                                "enabled": true
                              },
                              {
                                "value": 1.0,
                                "controlAddress": "/visitingBehaviour",
                                "enabled": true
                              }
                            ]
                          },
                          "noise": {
                            "parameters": [
                              {
                                "value": [
                                  0.300000011920929,
                                  0.1000000014901161
                                ],
                                "controlAddress": "/falsePositives",
                                "enabled": false
                              },
                              {
                                "value": [
                                  0.300000011920929,
                                  0.1000000014901161
                                ],
                                "controlAddress": "/falseNegatives",
                                "enabled": false
                              }
                            ]
                          }
                        },
                        "type": "SimulatorSource"
                      },
                      {
                        "parameters": [
                          {
                            "value": true,
                            "controlAddress": "/enabled"
                          },
                          {
                            "value": [
                              -704.0,
                              -254.1176452636719
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              240.0,
                              80.0
                            ],
                            "controlAddress": "/viewUISize"
                          },
                          {
                            "value": 1,
                            "hexMode": false,
                            "controlAddress": "/pointCount"
                          },
                          {
                            "value": 5.0,
                            "controlAddress": "/distanceThreshold"
                          }
                        ],
                        "niceName": "Outlier Removal",
                        "type": "Outlier Removal"
                      },
                      {
                        "parameters": [
                          {
                            "value": false,
                            "controlAddress": "/enabled"
                          },
                          {
                            "value": [
                              -1261.94873046875,
                              -262.5641174316406
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              240.0,
                              80.0
                            ],
                            "controlAddress": "/viewUISize"
                          },
                          {
                            "value": 0.001000000047497451,
                            "controlAddress": "/leafSize"
                          }
                        ],
                        "niceName": "Voxel Grid",
                        "type": "Voxel Grid"
                      },
                      {
                        "parameters": [
                          {
                            "value": [
                              -359.3846130371094,
                              -659.6923217773438
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              240.0,
                              80.0
                            ],
                            "controlAddress": "/viewUISize"
                          },
                          {
                            "value": "Filter",
                            "controlAddress": "/systemTag"
                          },
                          {
                            "value": true,
                            "controlAddress": "/sendToEditorOnly"
                          }
                        ],
                        "niceName": "Out filter",
                        "containers": {
                          "tag": {
                            "parameters": [
                              {
                                "value": "",
                                "controlAddress": "/tag"
                              }
                            ],
                            "niceName": "Tag",
                            "type": "Tag Selector"
                          }
                        },
                        "type": "Out"
                      },
                      {
                        "parameters": [
                          {
                            "value": [
                              171.2941131591797,
                              -252.2352905273438
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              240.0,
                              80.0
                            ],
                            "controlAddress": "/viewUISize"
                          },
                          {
                            "value": false,
                            "controlAddress": "/waitForAllInputs"
                          }
                        ],
                        "niceName": "Append Clusters",
                        "type": "Append Clusters"
                      },
                      {
                        "parameters": [
                          {
                            "value": true,
                            "controlAddress": "/enabled"
                          },
                          {
                            "value": [
                              -395.4871826171875,
                              -278.974365234375
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              240.0,
                              80.0
                            ],
                            "controlAddress": "/viewUISize"
                          },
                          {
                            "value": "C:/Users/Baptiste/Documents/espace_negatif/records_augmenta",
                            "controlAddress": "/directory"
                          },
                          {
                            "value": "rerecording_2",
                            "controlAddress": "/recordingFiles"
                          },
                          {
                            "value": true,
                            "controlAddress": "/forceV1Parsing"
                          },
                          {
                            "value": "ShowFinal26Juin22",
                            "controlAddress": "/recordFileName"
                          },
                          {
                            "value": false,
                            "controlAddress": "/overwrite"
                          },
                          {
                            "value": false,
                            "controlAddress": "/playAtLoad"
                          },
                          {
                            "value": true,
                            "controlAddress": "/passthroughEnabled"
                          },
                          {
                            "value": [
                              0.0,
                              1.0
                            ],
                            "controlAddress": "/loopRange"
                          }
                        ],
                        "niceName": "Cloud Recorder 1",
                        "type": "Cloud Recorder"
                      },
                      {
                        "parameters": [
                          {
                            "value": [
                              172.0,
                              -141.0
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              240.0,
                              80.0
                            ],
                            "controlAddress": "/viewUISize"
                          },
                          {
                            "value": "",
                            "controlAddress": "/recordingFiles"
                          },
                          {
                            "value": "mercredi4",
                            "controlAddress": "/recordFileName"
                          }
                        ],
                        "niceName": "Cluster Recorder 1",
                        "type": "Cluster Recorder"
                      },
                      {
                        "parameters": [
                          {
                            "value": [
                              -984.4705810546875,
                              -254.1176452636719
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              240.0,
                              80.0
                            ],
                            "controlAddress": "/viewUISize"
                          },
                          {
                            "value": false,
                            "controlAddress": "/isBlockingOutput"
                          }
                        ],
                        "niceName": "Conditional Check",
                        "type": "Conditional Check"
                      },
                      {
                        "parameters": [
                          {
                            "value": false,
                            "controlAddress": "/enabled"
                          },
                          {
                            "value": [
                              -982.0,
                              -141.0
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              240.0,
                              80.0
                            ],
                            "controlAddress": "/viewUISize"
                          },
                          {
                            "value": 3,
                            "hexMode": false,
                            "controlAddress": "/aliveTime"
                          }
                        ],
                        "niceName": "Temporal Denoising",
                        "type": "Temporal Denoising"
                      },
                      {
                        "parameters": [
                          {
                            "value": false,
                            "controlAddress": "/miniMode"
                          },
                          {
                            "value": [
                              -330.0,
                              -468.0
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              240.0,
                              80.0
                            ],
                            "controlAddress": "/viewUISize"
                          },
                          {
                            "value": "D:/Baptiste/Beats/Records",
                            "controlAddress": "/directory"
                          },
                          {
                            "value": "Blank",
                            "controlAddress": "/recordingFiles"
                          },
                          {
                            "value": true,
                            "controlAddress": "/forceV1Parsing"
                          },
                          {
                            "value": "Blank",
                            "controlAddress": "/recordFileName"
                          }
                        ],
                        "niceName": "Cloud Recorder",
                        "type": "Cloud Recorder"
                      },
                      {
                        "parameters": [
                          {
                            "value": [
                              -28.0,
                              -474.0
                            ],
                            "controlAddress": "/viewUIPosition"
                          },
                          {
                            "value": [
                              240.0,
                              80.0
                            ],
                            "controlAddress": "/viewUISize"
                          },
                          {
                            "value": "C:/Users/Baptiste/Documents/espace_negatif/records_augmenta",
                            "controlAddress": "/directory"
                          },
                          {
                            "value": "rerecording_3",
                            "controlAddress": "/recordingFiles"
                          },
                          {
                            "value": true,
                            "controlAddress": "/forceV1Parsing"
                          },
                          {
                            "value": "rerecording_4",
                            "controlAddress": "/recordFileName"
                          },
                          {
                            "value": false,
                            "controlAddress": "/overwrite"
                          }
                        ],
                        "niceName": "Cloud Recorder 2",
                        "type": "Cloud Recorder"
                      }
                    ],
                    "viewOffset": [
                      84,
                      323
                    ],
                    "viewZoom": 1.0,
                    "connections": {
                      "hideInEditor": true,
                      "items": [
                        {
                          "niceName": "Slot.out > One Euro Filter.In",
                          "type": "BaseItem",
                          "source": "slot",
                          "sourceSlot": "out",
                          "dest": "oneEuroFilter",
                          "destSlot": "In",
                          "connectionType": 4
                        },
                        {
                          "niceName": "One Euro Filter.out > Prediction.In",
                          "type": "BaseItem",
                          "source": "oneEuroFilter",
                          "sourceSlot": "out",
                          "dest": "prediction",
                          "destSlot": "In",
                          "connectionType": 4
                        },
                        {
                          "niceName": "Zone Process.Out Events > Out.Zones In",
                          "type": "BaseItem",
                          "source": "zoneProcess",
                          "sourceSlot": "Out Events",
                          "dest": "outDefault",
                          "destSlot": "Zones In",
                          "connectionType": 8
                        },
                        {
                          "niceName": "World Cameras.Out Clouds > Out 1.Clouds In",
                          "type": "BaseItem",
                          "source": "worldCameras",
                          "sourceSlot": "Out Clouds",
                          "dest": "outMerge",
                          "destSlot": "Clouds In",
                          "connectionType": 1
                        },
                        {
                          "niceName": "Euclidean Cluster.Out > Append Clusters.In",
                          "type": "BaseItem",
                          "source": "euclideanCluster",
                          "sourceSlot": "Out",
                          "dest": "appendClusters",
                          "destSlot": "In",
                          "connectionType": 4
                        },
                        {
                          "niceName": "SimulatorSource.Out > Append Clusters.In",
                          "type": "BaseItem",
                          "source": "simulatorSource",
                          "sourceSlot": "Out",
                          "dest": "appendClusters",
                          "destSlot": "In",
                          "connectionType": 4
                        },
                        {
                          "niceName": "Append Clusters.out > Tracker.In",
                          "type": "BaseItem",
                          "source": "appendClusters",
                          "sourceSlot": "out",
                          "dest": "tracker",
                          "destSlot": "In",
                          "connectionType": 4
                        },
                        {
                          "niceName": "Cluster Recorder 1.Out Clusters > Zone Process.Clusters In",
                          "type": "BaseItem",
                          "source": "clusterRecorder1",
                          "sourceSlot": "Out Clusters",
                          "dest": "zoneProcess",
                          "destSlot": "Clusters In",
                          "connectionType": 4
                        },
                        {
                          "niceName": "Cluster Recorder 1.Out Clusters > Out default.Clusters In",
                          "type": "BaseItem",
                          "source": "clusterRecorder1",
                          "sourceSlot": "Out Clusters",
                          "dest": "outDefault",
                          "destSlot": "Clusters In",
                          "connectionType": 4
                        },
                        {
                          "niceName": "Prediction.out > Cluster Recorder 1.In Clusters",
                          "type": "BaseItem",
                          "source": "prediction",
                          "sourceSlot": "out",
                          "dest": "clusterRecorder1",
                          "destSlot": "In Clusters",
                          "connectionType": 4
                        },
                        {
                          "niceName": "Voxel Grid.out > Conditional Check.In",
                          "type": "BaseItem",
                          "source": "voxelGrid",
                          "sourceSlot": "out",
                          "dest": "conditionalCheck",
                          "destSlot": "In",
                          "connectionType": 1
                        },
                        {
                          "niceName": "Conditional Check.out > Outlier Removal.In",
                          "type": "BaseItem",
                          "source": "conditionalCheck",
                          "sourceSlot": "out",
                          "dest": "outlierRemoval",
                          "destSlot": "In",
                          "connectionType": 1
                        },
                        {
                          "niceName": "World Cameras.Out Clouds > Voxel Grid.In",
                          "type": "BaseItem",
                          "source": "worldCameras",
                          "sourceSlot": "Out Clouds",
                          "dest": "voxelGrid",
                          "destSlot": "In",
                          "connectionType": 1
                        },
                        {
                          "niceName": "Tracker.out > Temporal Denoising.In",
                          "type": "BaseItem",
                          "source": "tracker",
                          "sourceSlot": "out",
                          "dest": "temporalDenoising",
                          "destSlot": "In",
                          "connectionType": 4
                        },
                        {
                          "niceName": "Temporal Denoising.out > Slot.In",
                          "type": "BaseItem",
                          "source": "temporalDenoising",
                          "sourceSlot": "out",
                          "dest": "slot",
                          "destSlot": "In",
                          "connectionType": 4
                        },
                        {
                          "niceName": "Outlier Removal.out > Cloud Recorder 1.In Cloud",
                          "type": "BaseItem",
                          "source": "outlierRemoval",
                          "sourceSlot": "out",
                          "dest": "cloudRecorder1",
                          "destSlot": "In Cloud",
                          "connectionType": 1
                        },
                        {
                          "niceName": "Cloud Recorder 1.Out Cloud > Cloud Recorder.In Cloud",
                          "type": "BaseItem",
                          "source": "cloudRecorder1",
                          "sourceSlot": "Out Cloud",
                          "dest": "cloudRecorder",
                          "destSlot": "In Cloud",
                          "connectionType": 1
                        },
                        {
                          "niceName": "Cloud Recorder.Out Cloud > Cloud Recorder 2.In Cloud",
                          "type": "BaseItem",
                          "source": "cloudRecorder",
                          "sourceSlot": "Out Cloud",
                          "dest": "cloudRecorder2",
                          "destSlot": "In Cloud",
                          "connectionType": 1
                        },
                        {
                          "niceName": "Cloud Recorder 2.Out Cloud > Out filter.Clouds In",
                          "type": "BaseItem",
                          "source": "cloudRecorder2",
                          "sourceSlot": "Out Cloud",
                          "dest": "outFilter",
                          "destSlot": "Clouds In",
                          "connectionType": 1
                        },
                        {
                          "niceName": "Cloud Recorder 2.Out Cloud > Euclidean Cluster.In",
                          "type": "BaseItem",
                          "source": "cloudRecorder2",
                          "sourceSlot": "Out Cloud",
                          "dest": "euclideanCluster",
                          "destSlot": "In",
                          "connectionType": 1
                        }
                      ],
                      "viewOffset": [
                        0,
                        0
                      ],
                      "viewZoom": 1.0
                    }
                  }
                },
                "type": "Scene"
              }
            ],
            "viewOffset": [
              0,
              0
            ],
            "viewZoom": 1.0
          },
          "metaParameters": {
            "viewOffset": [
              0,
              0
            ],
            "viewZoom": 1.0
          }
        },
        "type": "World"
      }
    ],
    "viewOffset": [
      0,
      0
    ],
    "viewZoom": 1.0,
    "tags": {
      "viewOffset": [
        0,
        0
      ],
      "viewZoom": 1.0
    }
  }
}