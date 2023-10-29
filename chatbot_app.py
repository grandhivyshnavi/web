import openai
import streamlit as st
from textblob import TextBlob

# OpenAI API Key
api_key = "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"

def ask_gpt3(question, conversation=[]):
    conversation.append({"role": "user", "content": question})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        api_key=api_key
    )

    assistant_reply = response['choices'][0]['message']['content']
    return assistant_reply

def perform_sentiment_analysis(user_input):
    # Create a TextBlob object
    analysis = TextBlob(user_input)
    
    # Get the polarity score of the input text
    sentiment_polarity = analysis.sentiment.polarity
    
    if sentiment_polarity > 0:
        return "Positive"
    elif sentiment_polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    st.title("Sentiment Analysis, Chatbot")
    st.sidebar.header("Chatbot")

    # User input for sentiment analysis
    user_input = st.text_area("Enter a text for sentiment analysis:")
    if st.button("Analyze Sentiment"):
        sentiment_result = perform_sentiment_analysis(user_input)
        st.write(f"Sentiment: {sentiment_result}")

    # Chatbot interaction
    user_question = st.text_input("Chatbot: Ask a question")
    if st.button("Ask GPT-3"):
        assistant_reply = ask_gpt3(user_question)
        st.write(f"Chatbot: {assistant_reply}")

if __name__ == "__main__":
    main()
