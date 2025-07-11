# Import LangGraph components to define the agent flow
from langgraph.graph import StateGraph, END

# Import agent functions for each step of the travel logic
from agents.collector import collect_preferences
from agents.recommender import recommend_destination
from agents.weather import get_weather_forecast
from agents.itinerary import generate_itinerary
from agents.budget_checker import check_budget

# Main planner function that performs all travel-related tasks
def travel_logic(state):
    # Step 1: Extract structured preferences from user input
    prefs = collect_preferences(state["input"])

    # Step 2: Recommend a destination based on preferences
    destination = recommend_destination(prefs)

    # Step 3: Fetch weather forecast for the destination
    weather = get_weather_forecast(destination)

    # Step 4: Generate a detailed day-by-day itinerary
    itinerary = generate_itinerary(destination, prefs["days"], prefs["interests"])

    # Step 5: Check if the itinerary fits the user's budget
    budget_result = check_budget(itinerary, prefs["budget"])

    # Return all results in a structured dictionary
    return {
        "preferences": prefs,
        "destination": destination,
        "itinerary": (
            f"🌍 Destination: {destination}\n\n"
            + weather + "\n\n"
            + itinerary + "\n\n"
            + "💸 Budget Check: " + budget_result
        )
    }

# Build a LangGraph with a single node named "planner"
graph = StateGraph(dict)

# Add the planning logic as a node
graph.add_node("planner", travel_logic)

# Set the entry point to start at the planner node
graph.set_entry_point("planner")

# Define that the flow ends after the planner node
graph.add_edge("planner", END)

# Compile the graph into an executable chain
travel_chain = graph.compile()
