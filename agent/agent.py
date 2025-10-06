from google.adk.agents import Agent, SequentialAgent
from .flow_capture import run_test_flow
from .prompt import greet_agent_instruction, greet_agent_description, start_caputre_agent_description, start_caputre_agent_instruction, test_manager_agent_description, generate_test_case_agent_description, generate_test_case_agent_instruction, redirect_to_testbuddyhtml_description, redirect_to_testbuddyhtml_instruction
from .helper import get_system_details, save_json_file, open_html_in_browser

# Greet Agent - Greets and gathers context about the app and test scenario
greet_agent = Agent(
    name="greet_agent",
    model="gemini-2.5-flash",
    description=greet_agent_description,
    instruction=greet_agent_instruction,
    tools=[get_system_details]
)

# Start Capture Agent - Initiates the automated browser test and recording
start_caputre_agent = Agent(
    name="start_capture_agent",
    model="gemini-2.5-pro",
    description=start_caputre_agent_description,
    instruction=start_caputre_agent_instruction,
    tools=[run_test_flow]
)

# Generate Test Case Agent - Creates comprehensive test cases based on the captured flow
generate_test_case_agent = Agent(
    name="generate_test_case_agent",
    model="gemini-2.5-pro",
    description=generate_test_case_agent_description,
    instruction=generate_test_case_agent_instruction,
    tools=[save_json_file]
)

# Redirect to TestBuddy HTML Agent - Opens the testbuddy.html file to view generated test cases
redirect_to_testbuddyhtml = Agent(
    name="redirect_to_testbuddyhtml",
    model="gemini-2.5-pro",
    description=redirect_to_testbuddyhtml_description,
    instruction=redirect_to_testbuddyhtml_instruction,
    tools=[open_html_in_browser]
)

# Test Manager Agent - Orchestrates the overall testing process
test_manager_agent = SequentialAgent(
    name="test_manager_agent",
    sub_agents=[greet_agent, start_caputre_agent, generate_test_case_agent, redirect_to_testbuddyhtml],
    description=test_manager_agent_description
)

# Root Agent - Entry point for the testing workflow
root_agent = test_manager_agent