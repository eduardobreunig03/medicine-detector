import os
import json
from openai import OpenAI
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

MEDICINE_KEYWORDS = [ "panadol", "nurofen", "aspirin", "ibuprofen", "tylenol", "advil", "voltaren", "zyrtec"]

def transcribe_audio(audio_file_path, api_key):
    client = OpenAI(api_key=api_key)
    
    
    with open(audio_file_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcript.text

def find_medicine_mentions(text):
    
    mentions = []
    text_lower = text.lower()
    
    for medicine in MEDICINE_KEYWORDS:
        if medicine in text_lower:
            mentions.append(medicine)
    
    return mentions

def save_results(mentions):
    
    output_file = "medicines.txt"
    
    with open(output_file, "w") as f:
        if mentions:
            for medicine in mentions:
                f.write(f"{medicine}.")
        else:
            f.write("No medicine mentions found . \n")

def main():
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("Error: OPENAI_API_KEY not found in .env file")
        
        return
    
    audio_file_path = input("Enter the path to the audio file: ")
    
    if not os.path.exists(audio_file_path):
        print(f"Error: File not found")
        
        return
    
    try:
        transcribed_text = transcribe_audio(audio_file_path, api_key)
        print(transcribed_text)
        mentions = find_medicine_mentions(transcribed_text)
        save_results(mentions)
        
        print(f"Results saved to medicine_mentions.txt")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 