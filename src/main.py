#!/usr/bin/env python
import openai
import os
import warnings
import tempfile
import sounddevice as sd
import numpy as np
import wave
from crew import Chalk, Chalk1
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Function to record and transcribe voice input using OpenAI Whisper
def listen():
    """Record audio from microphone and transcribe using OpenAI Whisper API."""
    print("Listening... Speak now.")

    fs = 44100  # Sampling rate
    duration = 5  # Duration of recording in seconds
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
    sd.wait()  # Wait until recording is complete

    # Save the recorded audio to a temporary WAV file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        with wave.open(temp_audio.name, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(fs)
            wf.writeframes(audio_data.tobytes())
        temp_audio_path = temp_audio.name

    # Transcribe the recorded audio using OpenAI Whisper
    try:
        with open(temp_audio_path, "rb") as audio_file:
            transcript = openai.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
    

        os.remove(temp_audio_path)  # Cleanup temporary file
        
        if transcript and transcript.text:
            print(f"You said: {transcript.text}")
            return transcript.text.lower()
        else:
            print("Sorry, I couldn't understand.")
            return None
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

# Function to convert AI response text to speech using OpenAI TTS
def speak(text):
    """Convert text to speech using OpenAI's TTS model and play it."""
    if not isinstance(text, str):
        print("Invalid text for speech synthesis.")
        return

    try:
        response = openai.audio.speech.create(
            model="tts-1",
            voice="alloy",  # Options: alloy, echo, fable, onyx, nova, shimmer
            input=text
        )

        # Save and play the generated speech
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            temp_audio.write(response.content)
            temp_audio_path = temp_audio.name

        print("AI: " + text)
        os.system(f"start {temp_audio_path}")  # Play the audio on Windows
    except Exception as e:
        print(f"Error in text-to-speech conversion: {e}")

# Function to manage conversation flow with the AI crew
def run_voice_conversation():
    """Manage a voice-based conversation with AI crew using STT and TTS."""
    conversation_crew = Chalk().crew()
    journal_crew = Chalk1().crew()
    
    user_messages = []
    speak("Hey! How are you? Say 'stop' to end the conversation.")
    
    while True:
        user_message = listen()
        if user_message in ['stop', 'bye', 'end']:
            speak("Ending the conversation. Summarizing and saving...")
            break
        
        if user_message:
            user_messages.append(user_message)

            # Get AI response
            response = conversation_crew.kickoff(inputs={'user_input': user_message})

            # Extract AI response safely
            if hasattr(response, 'get_final_output'):
                response_text = response.get_final_output()
            else:
                response_text = str(response)

            speak(response_text)

    # Save conversation summary
    journal_crew.kickoff(inputs={'user_messages': user_messages})
    speak("Your conversation has been saved. Goodbye!")
    user_messages.clear()

if __name__ == "__main__":
    run_voice_conversation()
