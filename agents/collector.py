# Import ChatOllama to use the local Mistral model via Ollama
from langchain_community.chat_models import ChatOllama

# Import ChatPromptTemplate to build structured LLM prompts
from langchain.prompts import ChatPromptTemplate

# Import json module for safely parsing the LLM output
import json

# Initialize the Ollama-based language model with the "mistral" model
llm = ChatOllama(model="mistral")


# Define a function to extract structured travel preferences from the user's input
def collect_preferences(user_input: str) -> dict:
    # Create a structured prompt asking for specific keys in JSON format
    prompt = ChatPromptTemplate.from_template("""
    Extract structured travel preferences from this message:
    "{user_input}"

    Return only valid JSON with keys:
    - destination (optional string)
    - days (int)
    - budget (int, in USD)
    - interests (string or list)

    Do not add explanations. Only output JSON.
    """)

    # Format the prompt with the actual user input
    prompt_value = prompt.format(user_input=user_input)

    # Print the prompt for debugging purposes
    print("DEBUG: Prompt sent to LLM:\n", prompt_value)

    # Invoke the LLM with the prompt
    response = llm.invoke(prompt_value)

    # Raise an error if the model returns no content or an invalid response object
    if not response or not hasattr(response, "content"):
        raise ValueError("LLM returned no content. Check Ollama is running.")

    # Try to parse the JSON string from the model's response content
    try:
        prefs = json.loads(response.content.strip())
    except json.JSONDecodeError:
        # Raise a clear error if parsing fails
        raise ValueError(f"Invalid JSON returned by LLM:\n{response.content}")

    # Return the structured dictionary of preferences
    return prefs
