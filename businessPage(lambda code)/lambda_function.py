'''
import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

'''

import json
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

def lambda_handler(event, context):
    fileLoader= FileSystemLoader(searchpath = "./")
    env = Environment(loader=fileLoader)
    template = env.get_template("eachBusiness.html")
    html = template.render()
    
    return {
        'statusCode': 200,
        'body': html,
        "headers": {
            "Content-Type": "text/html"
        }
    }
