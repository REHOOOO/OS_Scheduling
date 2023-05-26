import json

data = [{
    'name':'p1',
    'burst_time':30,
    'arrival_time':0,
    'priority': 2
    },
{
    'name':'p2',
    'burst_time':10,
    'arrival_time':4,
    'priority': 1
},
{
    'name':'p3',
    'burst_time':5,
    'arrival_time':10,
    'priority': 0
    },
{
    'name':'p4',
    'burst_time':10,
    'arrival_time':2,
    'priority': 2
    },
    ]

file_path = "./input2.json"
with open(file_path, 'w') as f:
    json.dump(data,f, indent="\t")
