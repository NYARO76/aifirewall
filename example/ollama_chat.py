import ollama


response = ollama.chat(
    model="gemma3:1b",
    options={"temperature": 0, "top_p": 1},
    messages=[
        {"role": "system", "content": "당신은 친절힌 한국인 비서입니다."},
        {
            "role": "user",
            "content": "기린의 이빨은 몇 게인가요?.",
        },
    ],
)

print(response["message"]["content"])
