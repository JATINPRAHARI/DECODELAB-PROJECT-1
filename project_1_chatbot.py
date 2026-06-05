
import time
from typing import Dict, Optional


class AIGatekeeper:
    """
    A rule-based chatbot that uses deterministic logic gates
    to match user intents with predefined responses.
    
    This is the "WHITE BOX" approach: 100% transparent,
    zero hallucination, pure algorithmic decision-making.
    """
    
    def __init__(self):
        """Initialize the knowledge base with intents and responses."""
        
        # Knowledge Base: Dictionary with 5+ intents for fast O(1) lookup
        self.knowledge_base: Dict[str, str] = {
            # Greeting intents
            'hello': 'Hi there! Welcome to DecodeLabs. How can I assist you today?',
            'hi': 'Hello! I\'m here to help. What do you need?',
            'hey': 'Hey! What\'s on your mind?',
            'greetings': 'Greetings! I\'m ready to help you.',
            'good morning': 'Good morning! Hope you\'re having a great day!',
            'good afternoon': 'Good afternoon! Let\'s get to work.',
            'good evening': 'Good evening! How can I help?',
            
            # Information requests
            'who are you': 'I\'m an AI Gatekeeper built by DecodeLabs. I handle rule-based logic and deterministic responses.',
            'what can you do': 'I can respond to greetings, answer basic questions, and help with project guidance!',
            'help': 'I can assist with questions about Project 1 (Chatbot) or Project 2 (Classification). What would you like to know?',
            'project 1': 'Project 1 is a Rule-Based AI Chatbot. It demonstrates control flow, logic gates, and dictionary-based knowledge base.',
            'project 2': 'Project 2 is Data Classification Using AI. It teaches supervised learning with KNN algorithm on the Iris dataset.',
            'iris dataset': 'The Iris dataset has 150 samples, 3 classes (Setosa, Versicolor, Virginica), and 4 features.',
            'knn': 'K-Nearest Neighbors is a simple supervised learning algorithm that classifies based on proximity.',
            'feature scaling': 'Feature scaling normalizes data to have mean=0 and variance=1, improving model performance.',
            
            # Status and meta questions
            'how are you': 'I\'m functioning optimally! Ready to assist you.',
            'what\'s up': 'Just waiting to help you with your AI journey!',
            'thanks': 'You\'re welcome! Glad I could help.',
            'thank you': 'My pleasure! Happy learning!',
            'cheers': 'Cheers! Keep coding!',
            
            # Exit intents
            'exit': 'exit_command',
            'quit': 'exit_command',
            'bye': 'Goodbye! Keep pushing your AI skills forward. See you next time!',
            'goodbye': 'Goodbye! Thanks for chatting. Good luck with your projects!',
        }
        
        # System state
        self.is_running = True
        self.interaction_count = 0
        
    def sanitize_input(self, user_input: str) -> str:
        """
        PHASE 1: INPUT & SANITIZATION
        
        Clean user input by:
        - Converting to lowercase (case-insensitive matching)
        - Removing leading/trailing whitespace
        - Removing extra punctuation
        
        Args:
            user_input: Raw user input string
            
        Returns:
            Cleaned input ready for logic gates
        """
        cleaned = user_input.lower().strip()
        # Remove trailing punctuation for better matching
        cleaned = cleaned.rstrip('!?.,:;')
        return cleaned
    
    def match_intent(self, cleaned_input: str) -> Optional[str]:
        """
        PHASE 2: INTENT MATCHING & LOGIC GATES
        
        Try to find exact match in knowledge base O(1).
        If not found, try partial matching as fallback.
        
        Args:
            cleaned_input: Sanitized user input
            
        Returns:
            Response string or None if no match
        """
        # Exact match (Constant time O(1))
        if cleaned_input in self.knowledge_base:
            return self.knowledge_base[cleaned_input]
        
        # Partial matching (Linear time O(n), fallback mechanism)
        for intent, response in self.knowledge_base.items():
            if intent in cleaned_input or cleaned_input in intent:
                return response
        
        return None
    
    def generate_response(self, user_input: str) -> str:
        """
        PHASE 3: RESPONSE GENERATION
        
        The complete logic skeleton:
        INPUT -> SANITIZATION -> INTENT MATCHING -> RESPONSE ENGINE
        
        Args:
            user_input: Raw user input
            
        Returns:
            AI response string
        """
        # Phase 1: Sanitization
        cleaned_input = self.sanitize_input(user_input)
        
        if not cleaned_input:  # Empty input handling
            return "I didn't catch that. Could you please rephrase?"
        
        # Phase 2: Intent Matching
        response = self.match_intent(cleaned_input)
        
        # Phase 3: Response Engine
        if response == 'exit_command':
            self.is_running = False
            return 'Goodbye! Keep pushing your AI skills forward. See you next time!'
        elif response:
            return response
        else:
            # Fallback: Default response for unknowns
            return f"I don't understand '{user_input}'. Try asking about projects, datasets, or algorithms!"
    
    def process_input(self, user_input: str) -> str:
        """
        Main processing function that orchestrates the entire pipeline.
        
        Args:
            user_input: User's message
            
        Returns:
            Chatbot's response
        """
        self.interaction_count += 1
        return self.generate_response(user_input)
    
    def display_welcome(self):
        """Display welcome message and instructions."""
        print("\n" + "="*70)
        print(" "*10 + "🤖 DECODELABS AI GATEKEEPER - PROJECT 1 🤖")
        print("="*70)
        print("\n📚 Welcome to the Rule-Based AI Chatbot!")
        print("   This chatbot uses deterministic logic gates and decision trees.")
        print("\n💡 Try asking about:")
        print("   • Greetings: 'hello', 'hi', 'hey'")
        print("   • Projects: 'project 1', 'project 2'")
        print("   • Concepts: 'knn', 'feature scaling', 'iris dataset'")
        print("   • Exit: 'exit', 'quit', 'bye'")
        print("\n" + "="*70 + "\n")
    
    def run(self):
        """
        THE HEARTBEAT: INFINITE LOOP
        
        Keeps the chatbot alive until 'exit' command.
        This demonstrates the while True pattern with break mechanism.
        """
        self.display_welcome()
        
        while self.is_running:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                response = self.process_input(user_input)
                print(f"\nChatbot: {response}\n")
                
            except KeyboardInterrupt:
                print("\n\nChatbot: Goodbye! Thanks for chatting.")
                break
            except Exception as e:
                print(f"Error: {e}")
                continue
        
        print("\n" + "="*70)
        print(f"Session ended. Total interactions: {self.interaction_count}")
        print("="*70 + "\n")


def main():
    """
    Entry point for the AI Chatbot.
    
    Instantiates the AIGatekeeper and runs the infinite loop.
    """
    chatbot = AIGatekeeper()
    chatbot.run()


if __name__ == "__main__":
    main()
