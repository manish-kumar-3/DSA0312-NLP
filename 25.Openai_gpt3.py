
import openai

# Set your OpenAI API key
openai.api_key = ""

def generate_text(prompt):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )
    
    return response.choices[0].text.strip()

user_prompt = input("Enter the prompt: ")
generated_text = generate_text(user_prompt)
print("Generated text:")
print(generated_text)
