# Import the ChatOllama model from the LangChain community
from langchain_community.chat_models import ChatOllama

# Initialize the local Ollama LLM with the Mistral model
llm = ChatOllama(model="mistral")

# Define a list of possible destinations to choose from
possible_places = ["Bali", "Cairns", "Gold Coast", "Bangkok"]

# Function to recommend the most suitable destination
# Takes structured user preferences as input (dict)
def recommend_destination(prefs: dict) -> str:
    # Prompt asks the model to choose the best matching destination
    # based on user interests and budget from a predefined list
    prompt = f"""
    The user is interested in: {prefs['interests']}
    Budget: ${prefs['budget']}
    From these options: {possible_places}, pick the most suitable destination based on the interest and budget. Return only the destination name.
    """
    # Invoke the model and return the destination as plain text (stripped of whitespace)
    return llm.invoke(prompt).content.strip()
