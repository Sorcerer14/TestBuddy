from .flow_capture import run_test_flow
from google.adk.agents import Agent

# test commit
root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description="Execute the run_test_flow function to start an automated browser test, which should launch the browser, begin recording the screen in real time, perform the defined test steps, capture all network requests and responses, and stop recording when the test flow completes, producing both a video file and a structured network log for analysis.",
    instruction="Run the run_test_flow function to initiate an automated browser test. The instruction includes: launching the browser, starting real-time screen recording, executing the defined test steps, capturing all network requests and responses, and stopping recording automatically when the test flow finishes. Ensure that the function produces both a video file of the browser session and a structured network log file for further analysis.",
    tools=[run_test_flow]
)