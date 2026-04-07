from flask import Blueprint, jsonify
# from .. import agent
import sys
import os

# Get the directory of the current script, then go up one level
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

# Now you can import your module normally
import agent

api_bp = Blueprint("api", __name__)

def say_hello():
    return "Hello from same method!"
    
@api_bp.get("/hello")
def hello_world():
    message = agent.say_hello()
    return message

@api_bp.get("/chat")
async def call_agent():
    message = await agent.chat("Tell me about maxwell")
    return message

@api_bp.get("/api/data")
def get_sample_data():
    return jsonify(
        {
            "data": [
                {"id": 1, "name": "Sample Item 1", "value": 100},
                {"id": 2, "name": "Sample Item 2", "value": 200},
                {"id": 3, "name": "Sample Item 3", "value": 300},
            ],
            "total": 3,
            "timestamp": "2024-01-01T00:00:00Z",
        }
    )
