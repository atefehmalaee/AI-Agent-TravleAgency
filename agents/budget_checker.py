# Import the ChatOllama class from the langchain_community module
from langchain_community.chat_models import ChatOllama

# Initialize the LLM using the 'mistral' model from your local Ollama installation
llm = ChatOllama(model="mistral")

# Define a function to evaluate whether the given itinerary fits within the user's budget
def check_budget(itinerary: str, budget: float) -> str:
    # Create a prompt asking the model to estimate budget fit based on the itinerary
    prompt = f"""
    Estimate if this itinerary fits within ${budget} USD. Be honest and brief:

    {itinerary}
    """
    # Send the prompt to the LLM and return the generated response (just the content part)
    return llm.invoke(prompt).content
