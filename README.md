<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
   
</head>
<body>

<h1>🎙️ AI Conversational Agent with Journaling 📝</h1>

<p>
This project is a voice-based AI assistant powered by <strong>CrewAI</strong>. It allows users to have personalized conversations with an AI, which remembers previous interactions and stores conversation summaries for future reference.
</p>

<h2>🚀 Features</h2>
<ul>
    <li><strong>Voice-based interaction 🎤</strong> - The AI listens to your speech, transcribes it, and responds in a human-like manner using OpenAI’s Whisper and TTS.</li>
    <li><strong>Personalized conversations 💬</strong> - The AI remembers past interactions and tailors responses accordingly.</li>
    <li><strong>Conversation journaling 📖</strong> - After each session, the conversation is summarized and stored.</li>
    <li><strong>CrewAI-powered agents 🤖</strong> - Multiple agents collaborate to provide seamless interactions.</li>
    <li><strong>Long-term memory storage 🧠</strong> - Conversation records are stored in a SQLite database.</li>
</ul>

<h2>🏗️ CrewAI Architecture</h2>
<p>
This project is powered by <strong>CrewAI</strong>, which enables autonomous AI agents to collaborate efficiently.
</p>
<ul>
    <li><strong>Conversation Agent 🤖</strong> - Engages in friendly chat, using stored data for personalization.</li>
    <li><strong>Journal Agent 📜</strong> - Summarizes and stores the conversation after the session ends.</li>
</ul>
<p>
CrewAI handles agent orchestration, ensuring a smooth experience.
</p>

<h2>🛠️ Installation</h2>

<h3>1️⃣ Clone the repository:</h3>
<pre>
git clone https://github.com/your-username/ai-conversation-journal.git
cd ai-conversation-journal
</pre>

<h3>2️⃣ Install dependencies:</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>3️⃣ Set up environment variables:</h3>
<p>Create a <code>.env</code> file and add:</p>
<pre>
OPENAI_API_KEY=your_openai_api_key
</pre>

<h2>▶️ Usage</h2>
<p>To start the AI assistant, run:</p>
<pre>
python main.py
</pre>
<p>Speak when prompted. Say <strong>"stop"</strong> to end the conversation.</p>

<h2>🏗️ Technical Details</h2>

<h3>Agents (agents.yaml)</h3>
<ul>
    <li><strong>Conversation Agent</strong> - Engages in hyper-personalized chats using past records.</li>
    <li><strong>Journal Agent</strong> - Summarizes and stores conversations.</li>
</ul>

<h3>Tasks (tasks.yaml)</h3>
<ul>
    <li><strong>Conversation Task</strong> - Manages real-time discussions.</li>
    <li><strong>Journaling Task</strong> - Saves conversation summaries.</li>
</ul>

<h3>Crew Setup (crew.py)</h3>
<ul>
    <li><strong>Chalk Crew 🗣️</strong> - Manages live conversations.</li>
    <li><strong>Chalk1 Crew 📖</strong> - Handles journaling and memory storage.</li>
</ul>

<h3>Main Execution (main.py)</h3>
<ul>
    <li>Speech-to-Text (Whisper API)</li>
    <li>AI Response Handling (CrewAI)</li>
    <li>Text-to-Speech (TTS API)</li>
    <li>Journaling with SQLite Storage</li>
</ul>

<h2>🤝 Contributing</h2>
<p>Feel free to submit issues and pull requests.</p>

</body>
</html>
