import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

def generate_chat_response(prompt_messages, model="text-davinci-002", max_tokens=1500, temperature=1):
    message_list = [{"role": msg["role"], "content": msg["content"]} for msg in prompt_messages]
    prompt_text = "This is a chatbot that speaks English.\n\nChatbot conversation:\n\n" + "\n".join([f"{msg['role']}: {msg['content']}" for msg in message_list])

    response = openai.Completion.create(
        engine=model,
        prompt=prompt_text,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
    )

    return response.choices[0].text.strip()


def chat():
    print("Welcome to the GPT Chatbot!")
    print("Type 'quit' to exit the chatbot.")
    
    conversation_history = []

    # ANSI escape codes for text colors
    USER_COLOR = "\033[94m"  # Blue
    CHATBOT_COLOR = "\033[92m"  # Green
    RESET_COLOR = "\033[0m"  # Reset color to default

    while True:
        user_input = input(f"{USER_COLOR}You: {RESET_COLOR}")

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        conversation_history.append({"role": "user", "content": user_input})
        response = generate_chat_response(conversation_history)
        conversation_history.append({"role": "assistant", "content": response})

        print(f"{CHATBOT_COLOR}Chatbot: {response}{RESET_COLOR}")


if __name__ == "__main__":
    chat()