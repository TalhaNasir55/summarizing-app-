
import streamlit as st
from transformers import pipeline

def main():
    st.title("AI Text Summarization App")

    # Input text area for user to enter the text
    input_text = st.text_area("Enter the text you want to summarize:", "")

    if st.button("Summarize"):
        if input_text:
            # Summarize the input text using the transformers pipeline
            summarizer = pipeline("summarization")
            summary = summarizer(input_text, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)

            # Display the summarized text
            st.subheader("Summary:")
            st.write(summary[0]['summary_text'])
        else:
            st.warning("Please enter some text to summarize.")

if __name__ == "__main__":
    main()
