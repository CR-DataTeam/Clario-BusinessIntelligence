# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:36:58 2024

@author: joshua.mcdonald
"""



def loginValidate():
    hmm = {
        "data": [
            "Login.access",
            [
                "joshua.mcdonald",
                "GgAYORgcSlZ+",
                "",
                "0"
            ]
        ],
        #"tid": 3,
        "login": 0,
        "app": "login",
        "action": "rpc",
        "method": "direct",
        "secure": None
    }
    return hmm


def loginHeaders():
    headers = {
                "Content-Type": "application/json; charset=utf-8", 
                } 
    return headers


def reportHeaders(cookie):
    cookie_text = "LoginDomain=; SESSION-SWL=" + cookie + "; active=analyse"
    headers = {
                "Content-Type": "application/json; charset=utf-8", 
                "Cookie":cookie_text
                }   
    return headers      


def generateReport(loginid, startDate="2024-07-01", endDate="2024-07-08"):
    um = {
        "data": [
            "report/type/Base.create",
            [
                "PhysicianProductivity",
                "19",
                {
                    "ws141": [
                        "1",
                        "2"
                    ],
                    "ws19": "",
                    "ws93": "",
                    "ws92": "",
                    "ws84": "",
                    "ws81": "",
                    "ws10": "",
                    "ws8": "",
                    "ws7": [
                        "90",
                        "91"
                    ],
                    "ws6": "",
                    "ws5": "",
                    "ws3": "",
                    "ws2": "",
                    "ws127": "",
                    "ws126": "",
                    "ws112": "",
                    "ws146": "",
                    "ws145": "",
                    "ws173": "",
                    "ws175": "",
                    "ws162": "rvu",
                    "ws113.site": "",
                    "ws113.location": "",
                    "ws83": "",
                    "ws79.db": "timeFReport",
                    "ws79.type": "abs",
                    "ws79.start": startDate,
                    "ws79.end": endDate,
                    "groupBy": "FK_priorityStatus"
                }
            ]
        ],
        #"tid": 165,
        "login": loginid,
        "app": "analyse",
        "action": "rpc",
        "method": "direct",
        "secure": None
    }
    return um


def inquiryReport(loginid):
    um = {
        "data": [
            "report",
        ],
        #"tid": 165,
        "login": loginid,
        "app": "analyse",
        "action": "rpc",
        "method": "direct",
        "secure": None
    }
    return um


def verboseReport(loginid, startDate="2024-08-01", endDate="2024-08-01"):
    payload =     {
        "data": [
            "report/type/Base.create",
            [
                "VerboseExport",
                "28",
                {
                    "ws79.db": "timeFReport",
                    "ws79.type": "abs",
                    "ws79.start": startDate,
                    "ws79.end": endDate,
                    "groupBy": "FK_priorityStatus"
                }
            ]
        ],
        #"tid": 717,
        "login": loginid,
        "app": "analyse",
        "action": "rpc",
        "method": "direct",
        "secure": None
    }
    return payload





              # "ws113.location": [
              #   "84"
              # ],

# "timeFReport",

def worklistQuery(loginid, startDate="2024-08-20", endDate="2024-08-21"):
    payload =     {
  "data": [
    {
      "params": {
        "input": {
          "ws7": [
            "50"
          ],
          "ws113.site": [
            "23",
            "28",
            "27"
          ],
          "ws113.location": [
              "233",
              "159",
              "235",
              "180",
              "244",
              "211",
              "176",
              "212",
              "184",
              "213",
              "209",
              "238",
              "187",
              "186",
              "210",
              "117",
              "106",
              "105",
              "94",
              "85",
              "84",
              "96",
              "95",
              "91",
              "93",
              "92",
              "82",
              "90"
            ],
        # "ws141": [
        #     "1",
        #     "2"
        # ],
          "ws26.db": "timeVerified",
          "ws26.type": "rel",
          "ws26.start": "2024-07-01"
          # "ws26.start": startDate,
          # "ws26.end": endDate
        },
        "type": "advanced",
        "isCountOnly": False,
        "limit": None
      },
      "call": "search/Exam.search",
      "sort": [
        {
          "property": "time",
          "direction": "ASC"
        }
      ],
      "operation": "user",
      "page": 1,
      "start": 0,
      "limit": None
    }
  ],
  "login": loginid,
  "app": "workflow",
  "action": "rpc",
  "method": "search",
  "secure": None
}   
    # {
    #   "data": [
    #     {
    #       "params": {
    #         "input": {
    #            "ws7": [
    #                "50"
    #            ],  
    #            "ws113.site": [
    #               "23",
    #               "28",
    #               "27"
    #             ],
    #           # "ws141": [
    #           #     "1",
    #           #     "2"
    #           # ],
    #           "ws26.db": "timeVerified",  
    #           "ws26.type": "abs",
    #         },
    #         "type": "advanced",
    #         "isCountOnly": False,
    #         "limit": None
    #       },
    #       "call": "search/Exam.search",
    #       "sort": [
    #         {
    #           "property": "defaultDirectSorting",
    #           "direction": "ASC"
    #         }
    #       ],
    #       "operation": "user",
    #       "page": 1,
    #       "start": 0,
    #       "limit": "2500"
    #     }
    #   ],
    #   "login": loginid,
    #   "app": "workflow",
    #   "action": "rpc",
    #   "method": "search",
    #   "secure": None
    # }
    return payload

def worklist_columns():
    return [ 'accession', 'assign', 'assign_createdUserID', 'assign_creation', 'assign_icon', 'assign_isLocked'
                 , 'assign_reason', 'assign_userID', 'cpt', 'editPriority', 'examBodyPart', 'examID', 'group'
                 , 'hasCommunication', 'hasExamNote', 'hasTech', 'location', 'modality', 'ordering', 'priority'
                 , 'procedureName', 'proRvu', 'radiologist', 'site', 'siteProcedureName', 'status', 'time'
                 , 'timeModified', 'timeTargetSort', 'timeVerified', 'version'
                 ]