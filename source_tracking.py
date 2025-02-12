import os
import subprocess
from tika import parser

def extract_metadata(video_path):
    try:
        raw_metadata = parser.from_file(video_path)
        return raw_metadata['metadata']
    except Exception as e:
        return {"error": str(e)}

def trace_video_source(video_path):
    metadata = extract_metadata(video_path)

    # Placeholder logic for tracing source
    if "producer" in metadata:
        source_info = f"Original Producer: {metadata['producer']}"
    elif "title" in metadata:
        source_info = f"Title: {metadata['title']}"
    else:
        source_info = "No clear source found."

    return source_info
