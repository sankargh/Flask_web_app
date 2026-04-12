from curses import def_prog_mode
from turtle import mode
from agents import Agent, Runner, function_tool, trace, WebSearchTool
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

text_agent = Agent(
        name="Text format agent",
        instructions="You are a text formatting agent. Your job is to format the given text \
             Convert main points as bulletin points \
            Wrap the longer text to multiple lines. Do not add more than 15 words per line\
            Do not modify the core content and facts ",
        model="gpt-4o-mini"
    )
    
text_tool=text_agent.as_tool(tool_name="Text_Formatter",tool_description="Format the given text to bullettin points")

local_event_websites=[
   "https://www.visitsingapore.com/whats-happening/all-happenings/",
   "https://www.eventbrite.sg/d/singapore--singapore/events/",
   "https://www.timeout.com/singapore/things-to-do/the-time-out-singapore-hotlist" 
]
local_agent = Agent(
    name="Local Agent",
    instructions=f"Tell me about in Singapore local events with tools provided \
        Use the 'WebSearchTool to get the local event updates from following websites \
            Websites List--> {local_event_websites} \
        Follow these thumbnail rules while giving information \
            1.  Prefer events that are Suitable for 'Family' \
            2.  Events should be in present or next 7 dasys from today \
        Share the result as List of events with 'Date, Place, Ticket price (if any) Highlighted  \
        Provide a clickable link at each result    ",
    tools=[WebSearchTool()],
    model="gpt-4o-mini"
)

gold_agent = Agent(
        name = "Gold rate",
        instructions="Check gold price from this URL --> 'https://goldprice.org/gold-price-india.html' \
                        Search the web using 'WebSearchTool' \
                        Result should have below format \
                        Example: -->    \
                        Here are the current gold rates in India: \
                        - **24 Karat (99.9% purity) Gold**: ₹15,284 per gram  \
                        - **22 Karat (91.6% purity) Gold**: ₹14,010 per gram  \
                        - **18 Karat (75% purity) Gold**: ₹11,463 per gram  \
                        *Source: Goodreturns (goodreturns.in)* \
                            ",
        tools = [WebSearchTool()],
        model="gpt-4o-mini"
)

#Local Event function definition
async def local(message):
    with trace("Test API from Git"):
        result = await Runner.run(local_agent,message)
    return str(result.final_output)

#Gold price function definition
async def get_goldrate(message):
    with trace("Get Gold rate"):
        result = await Runner.run(gold_agent,message)
    return str(result.final_output)
