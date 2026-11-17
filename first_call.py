import anthropic

client = anthropic.Anthropic()  #ANTHROPIC_API_KEY 환경 변수를 자동으로 읽음

res = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user"
            ,"content": "보험 약관에서 '면책 조항'이 무슨 뜻인지 3줄로 설명해줘"
        }
    ]
)

print(f"content ======  {res.content}")

answer = ""
for block in res.content:
    if block.type == "text":
        answer += block.text
print(answer)