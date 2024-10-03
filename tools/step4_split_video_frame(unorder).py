import os
import subprocess

# Obtain all video files in the current directory
videos = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.mp4')]

# Walk through each video file
for video in videos:
    # Create a folder named after the current video
    folder_name = os.path.splitext(video)[0]
    os.makedirs(folder_name, exist_ok=True)

    # Use FFmpeg to separate the video into multiple individual images and save them to a folder named after the video
    cmd = f"ffmpeg -i {video} -start_number 0 -r 24 {folder_name}/image_%05d.jpg"
    subprocess.call(cmd, shell=True)
