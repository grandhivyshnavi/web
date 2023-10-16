# Import necessary libraries
import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download NLTK resources
nltk.download('vader_lexicon')

# Load the sentiment analysis model
sid = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis
def analyze_sentiment(text):
    sentiment_score = sid.polarity_scores(text)
    if sentiment_score['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_score['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Function to build and train the chatbot
def build_chatbot():
    responses = {
        'greeting': 'Hello! How can I assist you today?',
        'goodbye': 'Goodbye! Have a great day!',
        'default': 'I am sorry, but I am not sure how to respond to that.'
    }
    return responses

# Function to get chatbot response
def get_chatbot_response(user_input, chatbot):
    # Simple rule-based chatbot
    if user_input.lower() in ['hi', 'hello', 'hey']:
        return chatbot['greeting']
    elif user_input.lower() in ['bye', 'goodbye']:
        return chatbot['goodbye']
    else:
        return chatbot['default']

# Streamlit web app
def main():
    # Set page title and icon
    st.set_page_config(page_title='Amazon Chatbot', page_icon=':robot_face:')

    # Set app title
    st.title('Amazon Chatbot')

    # User input for chatbot
    user_input = st.text_input('You:')

    # Build the chatbot
    chatbot = build_chatbot()

    # Get chatbot response
    chatbot_response = get_chatbot_response(user_input, chatbot)

    # Display chatbot response
    st.text_area('Chatbot:', value=chatbot_response, height=100)

    # Sentiment analysis
    st.header('Sentiment Analysis')
    user_text = st.text_input('Enter text for sentiment analysis:')
    if user_text:
        sentiment = analyze_sentiment(user_text)
        st.write('Sentiment:', sentiment)

if __name__ == '__main__':
    main()
