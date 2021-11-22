import json
import os
import sys
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

def lambda_handler(event, context):
    print(event)
    fileLoader= FileSystemLoader(searchpath = "./")
    env = Environment(loader=fileLoader)
    template = env.get_template("login.html")
    html = template.render()
    return {
        'statusCode': 200,
        'body': html,
        "headers": {
            "Content-Type": "text/html"
        }
    }
