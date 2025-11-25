import os
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
import requests
from io import BytesIO
from PIL import Image
import random

# Simple stock background options (royalty free)
BACKGROUND_IMAGES = [
    "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1",
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
    "https://images.unsplash.com/photo-1517694712202-14dd9538aa97",
    "https://images.unsplash.com/photo-1519389950473-47ba0277781c",
]

def generate_tts(text, out_path="voice.mp3"):
    """Generate audio narration using free Google TTS."""
    tts = gTTS(text=text, lang="en")
    tts.save(out_path)
    return out_path


def fetch_image(url):
    """Download an image from a URL."""
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    local_path = "background.jpg"
    img.save(local_path)
    return local_path


def generate_faceless_video(script_text, output="final_video.mp4"):
    """Create a faceless video using TTS + stock AI images."""
    
    print("Generating narration...")
    audio_path = generate_tts(script_text)

    print("Downloading background...")
    selected_image = random.choice(BACKGROUND_IMAGES)
    image_path = fetch_image(selected_image)

    print("Building video...")
    audio = AudioFileClip(audio_path)
    img_clip = ImageClip(image_path).set_duration(audio.duration)

    img_clip = img_clip.set_audio(audio)

    print("Saving final video...")
    img_clip.write_videofile(output, fps=24)

    return output
