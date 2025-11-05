from google import genai
from google.genai import types

client = genai.Client(
    api_key="sk-PTelE3zvHbuw8Qmhte45hg",
    http_options=types.HttpOptions(base_url="https://hubai.loe.gg")
)

print("Введите ваш промпт (или 'exit' для выхода):")

while True:
    user_prompt = input(">>> ")
    if user_prompt.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=user_prompt
    )
    print(response.text)
