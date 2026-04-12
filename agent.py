from flask import Blueprint, jsonify
import sys
import os

# Get the directory of the current script, then go up one level
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

# Now, import your module normally
import agent

api_bp = Blueprint("api", __name__)

def say_hello():
    return "Hello from same method!"
    
@api_bp.get("/hello")
def hello_world():
    message = agent.say_hello()
    return message

@api_bp.get("/about")
def about():
    message = "Hi, I'm learning AI and love building agents"
    return message

@api_bp.get("/local")
async def local():
    message = await agent.local("Give the information about local events in Singapore")
    return message

@api_bp.get("/gold")
async def get_goldrate():
    message = await agent.get_goldrate("Get current gold rate in India")
    return message
