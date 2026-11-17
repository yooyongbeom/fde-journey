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

#print(f"content ======  {res.content}")
answer = ""
for block in res.content:
    if block.type == "text":
        answer += block.text
print(answer)

print(type(res.content[0]))            # 객체 타입 확인
print(res.usage)                       # 토큰 수 → 비용 감각
print(res.model_dump_json(indent=2))   # 응답 전체 구조