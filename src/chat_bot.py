from openai import OpenAI
import os
from database import create_connection, create_table, save_message, load_chat_history

def initialize_chat_bot():
    conn = create_connection()
    create_table(conn)
    return conn

def generate_response(prompt, chat_history):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    
    for user_message, bot_response in chat_history:
        messages.append({"role": "user", "content": user_message})
        messages.append({"role": "assistant", "content": bot_response})
    
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response.choices[0].message.content.strip()