import openai

class ChatbotHandler:
    def __init__(self, api_key):
        openai.api_key = api_key

    def process_message(self, message):
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': message}]
        )
        return response['choices'][0]['message']['content']

# Example usage:
# chatbot = ChatbotHandler('your-api-key')
# reply = chatbot.process_message('Hello!')
# print(reply)