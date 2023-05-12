import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

def generate_text(prompt, model="text-davinci-002", max_tokens=150):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.4,
    )
    return response.choices[0].text.strip()

def chat():
    print("Welcome to the GPT Chatbot!")
    print("Type 'quit' to exit the chatbot.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        prompt = f"{user_input}"
        response = generate_text(prompt)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
