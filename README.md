# 🧭 AI Travel Planner

A smart travel assistant using Ollama (Mistral) to generate custom travel plans including destination suggestions, itinerary, weather forecast, and budget check.

## 🚀 Features
- Extracts structured preferences from user input
- Recommends suitable destinations
- Generates day-by-day itineraries
- Fetches weather forecast via Open-Meteo API
- Checks if trip fits within budget

## 🛠️ Tech Stack
- Python 3.11
- LangGraph
- LangChain + Ollama (Mistral)
- Open-Meteo API

## ▶️ How to Run

1. **Install Ollama & Run Mistral**  
   ```bash
   ollama run mistral
   ```

2. **Clone and Set Up Environment**  
   ```bash
   git clone https://github.com/your-username/ai-travel-planner.git
   cd ai-travel-planner
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the App**  
   ```bash
   python app.py
   ```

## 📂 Structure
```
ai-travel-planner/
├── agents/
├── graph/
├── app.py
├── README.md
```

## 📄 License
MIT License
