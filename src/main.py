import streamlit as st
from dotenv import load_dotenv
from chat_bot import initialize_chat_bot, generate_response, save_message, load_chat_history

load_dotenv()

def main():
    st.title("Context-Aware Chat Bot")

    USER_AVATAR = "👤"
    BOT_AVATAR = "🤖"
    
    conn = initialize_chat_bot()
    chat_history = load_chat_history(conn)

    user_input = st.text_input(USER_AVATAR)
    
    if user_input:
        bot_response = generate_response(user_input, chat_history)
        save_message(conn, user_input, bot_response)
        
        st.text_area(BOT_AVATAR, value=bot_response)
        
        chat_history.append((user_input, bot_response))

if __name__ == "__main__":
    main()