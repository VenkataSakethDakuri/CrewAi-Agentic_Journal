#!/usr/bin/env python
import sys
import warnings
import os
from dotenv import load_dotenv
from crew import Chalk


from crew import Chalk1

load_dotenv()
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Multi-round conversation with journaling.
    """
    conversation_crew = Chalk().crew()
    journal_crew = Chalk1().crew()

    user_messages = []

    

    while True:
        user_message = input("You: ")
        if user_message.lower() in ['end', 'stop', 'bye']:      
            print("Ending the conversation. Summarizing and saving...")
            break
        
        user_messages.append(user_message)

        # Kickoff conversation task
        conversation_crew.kickoff(inputs={'user_input': user_message})
    

    
    journal_crew.kickoff(inputs={'user_messages': user_messages})
    user_messages.clear()

run()

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Chalk().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Chalk().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Chalk().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
