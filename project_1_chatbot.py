import time
from typing import Dict, Optional

class AIGatekeeper:
    """Simple Rule-Based AI Chatbot for DecodeLabs Project 1."""
    
    def __init__(self):
        # Knowledge Base
        self.knowledge_base: Dict[str, str] = {
            'hello': 'Hi there! Welcome to DecodeLabs. How can I assist you today?',
            'hi': 'Hello! I\'m here to help. What do you need?',
            'hey': 'Hey! What\'s on your mind?',
            'good morning': 'Good morning! Hope you\'re having a great day!',
            'good afternoon': 'Good afternoon!',
            'good evening': 'Good evening! How can I help?',
            
            'who are you': 'I\'m an AI Gatekeeper built by DecodeLabs.',
            'what can you do': 'I can answer questions about projects and AI concepts.',
            'help': 'Ask me about Project 1, Project 2, KNN, or Iris dataset.',
            
            'project 1': 'Project 1 is this Rule-Based AI Chatbot.',
            'project 2': 'Project 2 is Data Classification using KNN on Iris dataset.',
            'iris dataset': 'The Iris dataset has 150 samples with 3 flower classes.',
            'knn': 'KNN is a simple algorithm that classifies based on nearest neighbors.',
            'feature scaling': 'Feature scaling normalizes data for better model performance.',
            
            'how are you': 'I\'m functioning optimally!',
            'thanks': 'You\'re welcome!',
            'thank you': 'My pleasure!',
            
            'exit': 'exit_command',
            'quit': 'exit_command',
            'bye': 'Goodbye! Keep pushing your AI skills forward.',
            'goodbye': 'Goodbye! Thanks for chatting.',
        }
        
        self.is_running = True
        self.interaction_count = 0

    def sanitize_input(self, user_input: str) -> str:
        """Clean and normalize user input."""
        cleaned = user_input.lower().strip()
        return cleaned.rstrip('!?.,:;')

    def match_intent(self, cleaned_input: str) -> Optional[str]:
        """Match user input with knowledge base."""
        if cleaned_input in self.knowledge_base:
            return self.knowledge_base[cleaned_input]
        
        # Partial matching fallback
        for intent, response in self.knowledge_base.items():
            if intent in cleaned_input or cleaned_input in intent:
                return response
        return None

    def generate_response(self, user_input: str) -> str:
        """Generate response based on user input."""
        cleaned_input = self.sanitize_input(user_input)
        
        if not cleaned_input:
            return "I didn't catch that. Could you please rephrase?"
        
        response = self.match_intent(cleaned_input)
        
        if response == 'exit_command':
            self.is_running = False
            return 'Goodbye! Keep pushing your AI skills forward.'
        elif response:
            return response
        else:
            return f"I don't understand '{user_input}'. Try asking about projects or KNN."

    def process_input(self, user_input: str) -> str:
        """Process user input and return response."""
        self.interaction_count += 1
        return self.generate_response(user_input)

    def display_welcome(self):
        """Show welcome message."""
        print("\n" + "="*60)
        print("     🤖 DECODELABS AI GATEKEEPER - PROJECT 1")
        print("="*60)
        print("Try asking: hello, project 1, knn, iris dataset, bye\n")

    def run(self):
        """Run the chatbot."""
        self.display_welcome()
        
        while self.is_running:
            try:
                user_input = input("You: ").strip()
                if not user_input:
                    continue
                
                response = self.process_input(user_input)
                print(f"\nChatbot: {response}\n")
                
            except KeyboardInterrupt:
                print("\n\nChatbot: Goodbye!")
                break
            except Exception:
                continue
        
        print(f"\nSession ended. Total interactions: {self.interaction_count}")

def main():
    chatbot = AIGatekeeper()
    chatbot.run()

if __name__ == "__main__":
    main()
