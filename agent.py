import gradio as gr
from agents import Agent, Runner, function_tool, trace
from dotenv import load_dotenv

load_dotenv(override=True)

# Hello Function definition
def say_hello():
    """Returns simple hello text."""
    return "Hello, World! I am an agent!"

# Maxwell Function definition
@function_tool
def about_maxwell():
    """ Gets detail about maxwell """
    return "Maxwell is an MRT in Singapore. It is part of 'Thompson East coast line'. The station is closer to China town"
    
agent = Agent(
    name="Test Agent",
    instructions="Tell me about in Singapore with tools provided",
    tools=[about_maxwell],
    model="gpt-4o-mini"
)

#Chat function definition
async def chat(message):
    with trace("Test API from Git"):
        result = await Runner.run(agent,message)
    return str(result.final_output)

# async def chat(user_input: str, history):
#     with trace("Test API from Git"):
#         result = await Runner.run(agent,user_input)
#     return result.final_output
# gr.ChatInterface(fn=chat).launch()
