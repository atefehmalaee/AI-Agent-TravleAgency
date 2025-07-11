# Import the ChatOllama model from the LangChain community integrations
from langchain_community.chat_models import ChatOllama

# Initialize the local LLM using the Mistral model served by Ollama
llm = ChatOllama(model="mistral")

# Define a function to generate a travel itinerary
# Takes destination, number of days, and user interests as input
def generate_itinerary(destination: str, days: int, interests: str) -> str:
    # Create a prompt asking the model to generate a day-by-day itinerary
    # customized to the user's destination and interests
    prompt = f"""
    Create a {days}-day itinerary for {destination} focused on {interests}.
    List activities day-by-day.
    """
    # Send the prompt to the model and return only the generated content (text)
    return llm.invoke(prompt).content
