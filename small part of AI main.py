client = Groq(api_key=os.getenv("GROQ_API_KEY"))
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "WAP to generate a paragraph on the inportance of sex education ",
        }
    ],
    model="openai/gpt-oss-120b",
)
print(print(chat_completion.choices[0].message.content))
