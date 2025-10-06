greet_agent_instruction = (
    """Greet the user warmly, ask how you can assist them today, 
    and collect details about the application and scenario they intend to record. 
    Forward this information to the next agent for processing."""

)
greet_agent_description = (
    """A friendly and interactive agent that welcomes users, gathers context about the app and test scenario,
    and initiates the test flow by passing the information to the next agent."""
)

start_caputre_agent_description = (
    """Execute the run_test_flow function to start an automated browser test, which should launch the browser, 
    begin recording the screen in real time, perform the defined test steps, 
    capture all network requests and responses, and stop recording when the test flow completes, 
    producing both a video file and a structured network log for analysis."""
)

start_caputre_agent_instruction = (
    """Run the run_test_flow function to initiate an automated browser test. 
    The instruction includes: launching the browser, 
    starting real-time screen recording, 
    executing the defined test steps, 
    capturing all network requests and responses, 
    and stopping recording automatically when the test flow finishes. 
    Ensure that the function produces both a video file of the browser session and a structured network log file for further analysis."""
)
generate_test_case_agent_description = (
    """Generate Positive Test cases, Negative Test cases, Regression, UI Interaction, Performance test, Data validation test (minimum 5 in each category) based on the captured test flow. 
    Each test case should include steps, expected outcomes, and relevant assertions for each category.
    Format the test cases as a JSON array, with each test case as an object containing 'title', 'test case type', 'steps', 'expected_outcome', 'assertions', and any additional relevant fields.
    Additionally, Gen AI will recommend when to test and how to test for each test case to support sustainability in testing practices.
    """
)

generate_test_case_agent_instruction = (
    """Create comprehensive test cases covering Positive, Negative, Regression, UI Interaction, Performance, and Data Validation scenarios. 
    For each category, outline the steps taken during the test flow, expected outcomes, and assertions to be validated. 
    Ensure the test cases are clear, structured, and suitable for implementation."""
)

test_manager_agent_description = (
    """Manages the flow between greeting the user, starting the test capture, and generating test cases."""
)

redirect_to_testbuddyhtml_description = (
    """Redirects to the testbuddy.html file to view the generated test cases."""
)

redirect_to_testbuddyhtml_instruction = (
    """Run the open_html_in_browser function to open the testBuddy.html file in the default web browser.
    This will display the generated test cases to the user."""
)
