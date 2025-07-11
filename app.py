# Import the compiled travel chain graph
from graph.travel_graph import travel_chain

# Load environment variables from a .env file (e.g., for API keys)
from dotenv import load_dotenv
load_dotenv()

# Main function to interact with the user
def main():
    # Display welcome message
    print("🌍 Welcome to the AI Travel Planner!")

    # Ask user to input travel preferences
    user_input = input("Tell me your travel preferences:\n> ")

    # Invoke the travel planner logic with user input
    result = travel_chain.invoke({"input": user_input})

    # Display the generated itinerary
    print("\n🧭 Your Itinerary:\n")
    print(result["itinerary"])

# Ensure the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()
