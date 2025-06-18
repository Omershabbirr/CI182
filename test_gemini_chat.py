import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from gemini_chat import get_response, main

class TestGeminiChat(unittest.TestCase):
    
    @patch('gemini_chat.model.generate_content')
    def test_get_response_success(self, mock_generate_content):
        # Mock the response from Gemini API
        mock_response = MagicMock()
        mock_response.text = "This is a test response"
        mock_generate_content.return_value = mock_response
        
        # Test the function
        result = get_response("What is the weather?")
        
        # Verify the response
        self.assertEqual(result, "This is a test response")
        mock_generate_content.assert_called_once()
        
        # Verify the prompt contains timestamp
        call_args = mock_generate_content.call_args[0][0]
        self.assertIn("[Current time:", call_args)
        self.assertIn("What is the weather?", call_args)

    @patch('gemini_chat.model.generate_content')
    def test_get_response_error(self, mock_generate_content):
        # Mock an API error
        mock_generate_content.side_effect = Exception("API Error")
        
        # Test the function
        result = get_response("What is the weather?")
        
        # Verify error handling
        self.assertEqual(result, "Error: API Error")

    @patch('builtins.input')
    @patch('builtins.print')
    @patch('gemini_chat.get_response')
    def test_main_quit(self, mock_get_response, mock_print, mock_input):
        # Mock user input to quit
        mock_input.return_value = "quit"
        
        # Run the main function
        main()
        
        # Verify the quit message was printed
        mock_print.assert_any_call("Goodbye!")

    @patch('builtins.input')
    @patch('builtins.print')
    @patch('gemini_chat.get_response')
    def test_main_empty_input(self, mock_get_response, mock_print, mock_input):
        # Mock empty input followed by quit
        mock_input.side_effect = ["", "quit"]
        
        # Run the main function
        main()
        
        # Verify empty input message
        mock_print.assert_any_call("Please enter a question.")

    @patch('builtins.input')
    @patch('builtins.print')
    @patch('gemini_chat.get_response')
    def test_main_normal_flow(self, mock_get_response, mock_print, mock_input):
        # Mock normal conversation flow
        mock_input.side_effect = ["What is Python?", "quit"]
        mock_get_response.return_value = "Python is a programming language"
        
        # Run the main function
        main()
        
        # Verify the response was printed
        mock_print.assert_any_call("\nResponse:", "Python is a programming language")

if __name__ == '__main__':
    unittest.main() 