<h1>🎙️ AI Conversational Agent with Journaling 📝</h1>


This project is a voice-based AI assistant powered by CrewAI. It allows users to have personalized conversations with an AI, which remembers previous interactions and stores conversation summaries for future reference.

🚀 Features
Voice-based interaction 🎤
The AI listens to your speech, transcribes it, and responds in a human-like manner using OpenAI’s Whisper and TTS.

Personalized conversations 💬
The AI remembers past interactions and tailors responses accordingly.

Conversation journaling 📖
After each session, the conversation is summarized and stored.

CrewAI-powered agents 🤖
Multiple agents collaborate to provide seamless interactions.

Long-term memory storage 🧠
Conversation records are stored in a SQLite database.

🏗️ CrewAI Architecture
This project is powered by CrewAI, which enables autonomous AI agents to collaborate efficiently.

Conversation Agent 🤖: Engages in friendly chat, using stored data for personalization.
Journal Agent 📜: Summarizes and stores the conversation after the session ends.
CrewAI handles agent orchestration, ensuring a smooth experience.

🛠️ Installation
1️⃣ Clone the repository:
git clone https://github.com/your-username/ai-conversation-journal.git
cd ai-conversation-journal

2️⃣ Install dependencies:
pip install -r requirements.txt

3️⃣ Set up environment variables:
Create a .env file and add:
OPENAI_API_KEY=your_openai_api_key

▶️ Usage
To start the AI assistant, run:
python main.py
Speak when prompted. Say "stop" to end the conversation.

🏗️ Technical Details
Agents (agents.yaml)

Conversation Agent: Engages in hyper-personalized chats using past records.

Journal Agent: Summarizes and stores conversations.

Tasks (tasks.yaml)

Conversation Task: Manages real-time discussions.

Journaling Task: Saves conversation summaries.

Crew Setup (crew.py)

Chalk Crew 🗣️: Manages live conversations.

Chalk1 Crew 📖: Handles journaling and memory storage.

Main Execution (main.py)

Speech-to-Text (Whisper API)

AI Response Handling (CrewAI)

Text-to-Speech (TTS API)

Journaling with SQLite Storage

🤝 Contributing
Feel free to submit issues and pull requests.
