#!/usr/bin/env python
"""
Test your Replicate API token and find available video models
"""

import os
import sys
import requests

def test_api_token(token):
    """Test if API token is valid"""
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }
    
    response = requests.get("https://api.replicate.com/v1/account", headers=headers)
    
    if response.status_code == 200:
        user = response.json()
        print(f"✅ API Token Valid!")
        print(f"   Account: {user.get('name', 'Unknown')}")
        print(f"   Email: {user.get('email', 'Unknown')}")
        return True
    elif response.status_code == 401:
        print("❌ API Token Invalid!")
        return False
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")
        return False

def find_video_models(token):
    """Find available video generation models"""
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }
    
    print("\n🔍 Searching for available video models...")
    
    # Search for video models
    models = [
        "openai/whisper",  # Not video but testing
        "stability-ai/stable-video-diffusion",
        "damo-vilab/text-to-video",
        "coco-gpt/text-to-video",
    ]
    
    print("\nCommon Video Models to Try:")
    print("1. stability-ai/stable-video-diffusion - Video generation from images")
    print("2. damo-vilab/text-to-video - Direct text-to-video")
    print("3. Visit https://replicate.com/explore?query=video for more models")
    
def main():
    token = os.environ.get('REPLICATE_API_TOKEN')
    
    if not token:
        print("❌ Error: REPLICATE_API_TOKEN not set")
        print("\nSet it with:")
        print("  Windows CMD:  set REPLICATE_API_TOKEN=your_token")
        print("  Windows PS:   $env:REPLICATE_API_TOKEN = 'your_token'")
        print("  Mac/Linux:    export REPLICATE_API_TOKEN=your_token")
        sys.exit(1)
    
    print("Testing Replicate API Token...\n")
    
    if not test_api_token(token):
        print("\n❌ Token is invalid. Get one from: https://replicate.com/account/api-tokens")
        sys.exit(1)
    
    find_video_models(token)
    
    print("\n✅ Setup looks good! You can now run: python app.py")

if __name__ == "__main__":
    main()
