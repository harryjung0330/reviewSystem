import json
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

def lambda_handler(event, context):
    fileLoader= FileSystemLoader(searchpath = "./")
    env = Environment(loader=fileLoader)
    template = env.get_template("registration.html")
    html = template.render()
    
    return {
        'statusCode': 200,
        'body': html,
        "headers": {
            "Content-Type": "text/html"
        }
    }
