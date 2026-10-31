from .Nodes import Nodes


graph = {
    "Ahmedabad": {
        "Indore": 390,
        "Surat": 267
    },

    "Surat": {
        "Ahmedabad": 267,
        "Mumbai": 284,
        "Nashik": 246
    },

    "Mumbai": {
        "Surat": 284,
        "Nashik": 166,
        "Pune": 148,
        "Kolhapur": 386
    },

    "Nashik": {
        "Surat": 246,
        "Mumbai": 166,
        "Indore": 419,
        "Nanded": 440
    },

    "Indore": {
        "Ahmedabad": 390,
        "Bhopal": 196,
        "Nagpur": 449,
        "Nashik": 419
    },

    "Bhopal": {
        "Indore": 196,
        "Jabalpur": 328
    },

    "Jabalpur": {
        "Bhopal": 328,
        "Nagpur": 275,
        "Raipur": 353
    },

    "Nagpur": {
        "Indore": 449,
        "Jabalpur": 275,
        "Raipur": 342,
        "Nanded": 342,
        "Hyderabad": 501
    },

    "Raipur": {
        "Jabalpur": 353,
        "Nagpur": 342,
        "Ranchi": 588,
        "Visakhapatnam": 549
    },

    "Ranchi": {
        "Raipur": 588,
        "Durgapur": 262,
        "Bhubaneswar": 460
    },

    "Durgapur": {
        "Ranchi": 262
    },

    "Bhubaneswar": {
        "Ranchi": 460,
        "Visakhapatnam": 441
    },

    "Visakhapatnam": {
        "Raipur": 549,
        "Bhubaneswar": 441,
        "Vijayawada": 344,
        "Hyderabad": 616
    },

    "Nanded": {
        "Nashik": 440,
        "Pune": 450,
        "Nagpur": 342,
        "Hyderabad": 276
    },

    "Pune": {
        "Mumbai": 148,
        "Nanded": 450,
        "Solapur": 253,
        "Kolhapur": 231
    },

    "Solapur": {
        "Pune": 253,
        "Hyderabad": 312,
        "Gulbarga": 128
    },

    "Kolhapur": {
        "Mumbai": 386,
        "Pune": 231,
        "Gulbarga": 323,
        "Hubli": 201
    },

    "Gulbarga": {
        "Solapur": 128,
        "Kolhapur": 323,
        "Hyderabad": 231
    },

    "Hubli": {
        "Kolhapur": 201,
        "Kurnool": 362,
        "Bengaluru": 412
    },

    "Hyderabad": {
        "Nagpur": 501,
        "Nanded": 276,
        "Solapur": 312,
        "Gulbarga": 231,
        "Kurnool": 212,
        "Vijayawada": 274,
        "Visakhapatnam": 616
    },

    "Kurnool": {
        "Hyderabad": 212,
        "Hubli": 362,
        "Bengaluru": 359
    },

    "Bengaluru": {
        "Hubli": 412,
        "Kurnool": 359,
        "Chennai": 347
    },

    "Vijayawada": {
        "Hyderabad": 274,
        "Visakhapatnam": 344,
        "Chennai": 451
    },

    "Chennai": {
        "Bengaluru": 347,
        "Vijayawada": 451
    }
}

heuristic_mapping = {
    "Indore":{
        "Ahmedabad": 338,
        "Jabalpur": 425,
        "Ranchi": 969,
        "Durgapur": 1174,
        "Bhubaneswar": 1065,
        "Surat": 356,
        "Nagpur": 376,
        "Raipur": 617,
        "Nashik": 370,
        "Nanded": 426,
        "Visakhapatnam": 950,
        "Mumbai": 509,
        "Pune": 511,
        "Solapur": 562,
        "Hyderabad": 653,
        "Vijayawada": 853,
        "Gulbarga": 607,
        "Kolhapur": 689,
        "Hubli": 821,
        "Kurnool": 799,
        "Bengaluru": 1099,
        "Chennai": 1168,
        "Bhopal": 170,
        "Indore": 0
    }
}

class Map:
    def __init__(self,start_node:Nodes,goal:str,path:bool=False,heuristic:bool=False):
        self.start_node=start_node
        self.goal=goal
        self.heurisitc=heuristic
        self.path=path
        if self.heurisitc:
            self.start_node.heuristic_cost=heuristic_mapping[self.goal][self.start_node.city]

    def neighbours(self,parent_node:Nodes,city_cost:int=0):
        city=parent_node.city

        if city==self.goal:
            print("Already reached:")

        response=[]
        for i in graph[city].keys():
            pcost=0
            hcost=0
            if self.path:
                pcost=city_cost+graph[city][i]
            if self.heurisitc:
                hcost=heuristic_mapping[self.goal][i]
            response.append(Nodes(
                parent=parent_node,
                city=i,
                current_cost=pcost,
                heuristic_cost=hcost
            ))

        return response