from openai import OpenAI

API_KEY = "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"

if API_KEY == "COLE_SUA_API_KEY_AQUI" or not API_KEY.strip():
    raise RuntimeError("Cole sua API key na variável API_KEY em ia.py")

client = OpenAI(api_key=API_KEY)

resposta = client.responses.create(
    model="gpt-4.1-mini", input="Explique como se forma o basalto."
)

print(resposta.output_text)
