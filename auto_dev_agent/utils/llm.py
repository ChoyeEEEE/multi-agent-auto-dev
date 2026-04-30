from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def call_llm(system_prompt, user_prompt):
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3
    )
    return res.choices[0].message.content
