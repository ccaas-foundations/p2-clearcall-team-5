"""Transcript Generator is designed to generate the rules of a creating, writing, repeating one call transcript.
The __init__ stores the config, helper methods generate the pieces, and the main method generates many files to output directory."""
from pathlib import Path
import random
from datetime import datetime, timedelta, timezone
from CallTranscript import CallTranscript

class TranscriptGenerator:
    def __init__(self, output_dir, agent_ids):
        self.output_dir = Path(output_dir)
        self.agent_ids = agent_ids
        self.categories = ["BILLING", "TECHNICAL", "SALES", "GENERAL"]
        self.category_weights = [40, 35, 15, 10]
    
    #returns string from list of categories randomly using weights
    def get_call_category(self):
        #returns one element
        return random.choices(self.categories, weights=self.category_weights, k=1)[0]
    
    #rules for getting ivr containment
    def get_ivr_containment(self, category):
        if category == "BILLING":
            return random.random() < 0.60
        elif category == "TECHNICAL":
            return False
        elif category == "SALES":
            return False
        elif category == "GENERAL":
            return random.random() < 0.40
        
    #assigns random agent, otherwise, its contained
    def get_agent_id(self, ivr_contained):
        if ivr_contained:
            return None
        return random.choice(self.agent_ids)
    
    def generate_times(self, category):
        now = datetime.now(timezone.utc)

        # random start time sometime in the last 30 days
        minutes_ago = random.randint(0, 30 * 24 * 60)
        start_time = now - timedelta(minutes=minutes_ago)

        if category == "BILLING":
            duration_seconds = random.randint(120, 420)
        elif category == "TECHNICAL":
            duration_seconds = random.randint(300, 900)
        elif category == "SALES":
            duration_seconds = random.randint(240, 720)
        else:  # GENERAL
            duration_seconds = random.randint(90, 360)

        end_time = start_time + timedelta(seconds=duration_seconds)
        return start_time, end_time
    
    def generate_transcript(self):
        pass
    def write_transcript(self, transcript):
        pass
    def generate_many(self, count=50):
        for _ in range(count):
            transcript = self.generate_transcript()
            self.write_transcript(transcript)