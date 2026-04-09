#force rebuild for deployment
import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

st.set_page_config(page_title="Carnival Feedback Analyzer", layout="wide")

st.title("🎪 Carnival Feedback Analyzer")
st.markdown("Upload a CSV of attendee feedback to see sentiment insights. *(Built as a demo project for NUS/NTU application portfolio)*")

# Sidebar for file upload
with st.sidebar:
    st.header("Upload Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    st.markdown("---")
    st.markdown("**Expected CSV Format:**")
    st.markdown("""
    `rating`, `comment`  
    `5`, `"Loved the music and lights!"`  
    `3`, `"Queue for food was too long."`  
    `5`, `"Amazing event, well organized."`  
    `1`, `"Couldn't hear the announcements."`
    """)

if uploaded_file is not None:
    # Load data
    df = pd.read_csv(uploaded_file)
    
    # Display raw data
    st.subheader("📋 Raw Feedback Sample")
    st.dataframe(df.head(10))
    
    # Check if required columns exist
    if 'comment' not in df.columns:
        st.error("CSV must contain a 'comment' column.")
        st.stop()
        
    # Sentiment Analysis Function
    def get_sentiment(text):
        analysis = TextBlob(str(text))
        polarity = analysis.sentiment.polarity

        if polarity > 0.1:
            return "Positive"
        elif polarity < 0.0:  
            return "Negative"
        else:
            return "Neutral"
    
    # Apply sentiment analysis
    with st.spinner("Analyzing feedback..."):
        df['sentiment'] = df['comment'].apply(get_sentiment)
    
    # --- Metrics Row ---
    col1, col2, col3 = st.columns(3)
    sentiment_counts = df['sentiment'].value_counts()
    
    with col1:
        pos_count = sentiment_counts.get('Positive', 0)
        st.metric("😊 Positive Comments", pos_count)
    with col2:
        neu_count = sentiment_counts.get('Neutral', 0)
        st.metric("😐 Neutral Comments", neu_count)
    with col3:
        neg_count = sentiment_counts.get('Negative', 0)
        st.metric("😞 Negative Comments", neg_count)
    
    # --- Charts Row ---
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.subheader("Sentiment Distribution")
        fig, ax = plt.subplots()
        ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90, colors=['#2ecc71', '#f1c40f', '#e74c3c'])
        ax.axis('equal')
        st.pyplot(fig)
    
    with col_chart2:
        st.subheader("Common Words in Feedback")
        # Generate Word Cloud
        text = " ".join(comment for comment in df['comment'].astype(str))
        # Add custom stopwords
        stopwords = set(STOPWORDS)
        stopwords.update(["event", "carnival", "will", "can", "get", "one", "like", "just"])
        
        wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=stopwords, colormap='viridis').generate(text)
        fig_wc, ax_wc = plt.subplots()
        ax_wc.imshow(wordcloud, interpolation='bilinear')
        ax_wc.axis("off")
        st.pyplot(fig_wc)
    
    # --- Actionable Insights ---
    st.subheader("💡 Actionable Insights for Future Events")
    if neg_count > 0:
        negative_comments = df[df['sentiment'] == 'Negative']['comment'].head(5).tolist()
        st.markdown("**Top areas for improvement (based on negative comments):**")
        for i, comment in enumerate(negative_comments, 1):
            st.markdown(f"- *\"{comment}\"*")
    else:
        st.success("No significant negative feedback detected. Great job!")
        
else:
    st.info("👈 Please upload a CSV file to begin analysis. Use the sample format in the sidebar.")
