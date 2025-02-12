import streamlit as st
import cv2
import tempfile
import os
import torch
from utils.deepfake_detection import analyze_video
from utils.source_tracing import trace_video_source

st.title("Deepfake Video Detection & Source Tracing")

# Upload video
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

if uploaded_file:
    # Save to a temp file
    temp_video = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_video.write(uploaded_file.read())
    temp_path = temp_video.name

    st.video(temp_path)  # Display uploaded video

    # Analyze video for deepfake detection
    with st.spinner("Analyzing video..."):
        is_fake, confidence = analyze_video(temp_path)
        st.subheader("Deepfake Detection Result")
        st.write(f"**Fake:** {is_fake}")
        st.write(f"**Confidence:** {confidence:.2f}%")

    # Source tracing
    with st.spinner("Tracing video source..."):
        source_details = trace_video_source(temp_path)
        st.subheader("Source Details")
        st.write(source_details)

    # Cleanup temp file
    os.remove(temp_path)
