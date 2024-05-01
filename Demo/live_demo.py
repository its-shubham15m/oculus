import streamlit as st

def show_live_demo():
    st.header("Live Demo")

    st.write("Here's a live demo with a video player.")

    # You can replace the video URL with your own video file URL
    video_url = "https://youtu.be/zPlR4Z3iF8A?si=T0SsHjWM8Acaii1o"

    st.video(video_url)
