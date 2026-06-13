# AI Video Generator - Setup Guide

## Prerequisites

1. **Get Replicate API Token**
   - Go to: https://replicate.com/signin
   - Sign up (free account)
   - Copy your API token from: https://replicate.com/account/api-tokens

2. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create `.env` from `.env.example`**
   ```bash
   copy .env.example .env
   ```

4. **Set Environment Variable**
   
   If you created a `.env` file, just run:
   ```bash
   python app.py
   ```
   
   Otherwise, set the token in your shell before running.
   
   **Windows (Command Prompt):**
   ```cmd
   set REPLICATE_API_TOKEN=your_api_token_here
   python app.py
   ```
   
   **Windows (PowerShell):**
   ```powershell
   $env:REPLICATE_API_TOKEN = "your_api_token_here"
   python app.py
   ```
   
   **macOS/Linux:**
   ```bash
   export REPLICATE_API_TOKEN=your_api_token_here
   python app.py
   ```
   ```bash
   export REPLICATE_API_TOKEN=your_api_token_here
   python app.py
   ```
   
   **Or create .env file:**
   ```
   REPLICATE_API_TOKEN=your_api_token_here
   ```

## Run the Application

### Local Development
```bash
python app.py
```
Then open: http://localhost:5000/

### Deploy to Railway
1. Push code to GitHub
2. Connect GitHub to Railway.app
3. Set environment variable `REPLICATE_API_TOKEN` in Railway dashboard
4. Deploy!

## Features
✅ Text-to-Video generation using multiple AI models
✅ Modern UI with loading states
✅ Error handling & validation
✅ CORS enabled
✅ Video history API
✅ Fallback models for reliability

## Video Generation Models
The app automatically tries multiple models:
1. **DreamTalk** (Primary) - High quality video generation
2. **Deforum** (Fallback 1) - Fast video generation
3. **DAMO Text-to-Video** (Fallback 2) - Alternative model

Processing time: 1-5 minutes per video (depending on model)

## Troubleshooting

### "404 Error - Resource Not Found"
This means the model is not available in your region. Solutions:
1. Check your API token is valid: https://replicate.com/account/api-tokens
2. Try a different model from: https://replicate.com/explore?query=video
3. Test API token with: `curl -H "Authorization: Token $REPLICATE_API_TOKEN" https://api.replicate.com/v1/account`

### "No videos generating"
1. Verify API token is set correctly
2. Check console for error messages
3. Try a different, simpler prompt
4. Check Replicate.com for model availability in your region

### Get Working Model IDs
Visit: https://replicate.com/explore?query=video
Copy the model name and paste it in app.py

## API Endpoints

### POST /generate
```json
{
  "prompt": "A cat dancing in the rain"
}
```

Response:
```json
{
  "success": true,
  "video_id": "video_20260504_120000",
  "prompt": "A cat dancing in the rain",
  "video_url": "https://...mp4",
  "message": "Video generated successfully!"
}
```

### GET /videos
Get all generated videos

### GET /video/<video_id>
Get specific video details

## Need Help?
- Replicate Docs: https://replicate.com/docs
- Available Models: https://replicate.com/explore?query=video
- API Status: https://status.replicate.com

