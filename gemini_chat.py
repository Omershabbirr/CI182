import google.generativeai as genai
import os
from datetime import datetime

# Configure the Gemini API
GOOGLE_API_KEY = "AIzaSyAwaLDoH30REhsLYVV3jZZ3luTyL4iDZtI"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-2.5-flash')

def get_response(question):
    try:
        # Add timestamp to the question to emphasize real-time nature
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        prompt = f"[Current time: {current_time}] {question}"
        
        # Generate response
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Welcome to Gemini Chat! Type 'quit' to exit.")
    print("Ask any question about current events or any topic:")
    
    while True:
        user_input = input("\nYour question: ").strip()
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
            
        if not user_input:
            print("Please enter a question.")
            continue
            
        response = get_response(user_input)
        print("\nResponse:", response)

if __name__ == "__main__":
    main() 