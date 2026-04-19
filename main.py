import openai

def chat_with_ai():
    openai.api_key = "YOUR_API_KEY"

    print("Welcome to AI Chat! Type 'exit' to quit.")
    history = []

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        history.append({"role": "user", "content": user_input})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=history
            )

            reply = response['choices'][0]['message']['content']
            print(f"AI: {reply}")

            history.append({"role": "assistant", "content": reply})

        except openai.error.OpenAIError as e:
            print(f"Error: {e}")

# Run the tool
if __name__ == "__main__":
    chat_with_ai()