## 🚨 404 Error - Model Not Found

### What's the Problem?
The Replicate model ID is not available or doesn't exist in your region/account tier.

---

## ✅ SOLUTION

### Step 1: Test Your API Token
```bash
python test_api.py
```

This will:
- ✅ Verify your token is valid
- ✅ Show your account info
- ✅ List available models

### Step 2: Find a Working Model

**Option A: Use Model Explorer (BEST)**
1. Go to: https://replicate.com/explore?query=video
2. Look for models that say "text-to-video" or "video"
3. Click on a model (e.g., "stability-ai/stable-video-diffusion")
4. Copy the full model name

**Option B: Use These Tested Models**

```python
# Model 1: Stability AI Video Diffusion
"stability-ai/stable-video-diffusion:3f0457e4619daec51aa397344d6cb033ea0994e8"

# Model 2: DAMO Video Generation  
"damo-vilab/text-to-video-ms:e0b33a17e30a5eaf86dc4dcc5c5d6a20c92f36d7"

# Model 3: Cog Text-to-Video
"coco-gpt/text-to-video:03cd87dd"
```

### Step 3: Update app.py

1. Open `app.py`
2. Find the line with `replicate.run("`
3. Replace the model ID with one that works:

```python
output = replicate.run(
    "stability-ai/stable-video-diffusion:3f0457e4619daec51aa397344d6cb033ea0994e8",
    input={
        "prompt": prompt,
    }
)
```

### Step 4: Test Again
```bash
python test_api.py
python app.py
```

---

## 🔍 Troubleshooting

### Still Getting 404?
1. Make sure the model ID is EXACTLY correct (copy-paste from Replicate)
2. Check your API token is correct
3. Try a different model
4. Your account tier might not have access - check Replicate limits

### Getting Timeout?
- Video generation takes 2-5 minutes
- Wait for the process to complete
- Check Replicate dashboard for queue status

### API Token Issues?
1. Get a new token: https://replicate.com/account/api-tokens
2. Test it: `python test_api.py`
3. Make sure it's set as environment variable

---

## 📌 Quick Reference

**Current Fallback Models (Automatic):**
1. DreamTalk (Primary)
2. Deforum (Fallback)  
3. DAMO (Secondary Fallback)

If all fail, you'll get detailed error with hints.

**Manual Model Search:**
- Go to: https://replicate.com/explore?query=video
- Sort by "trending"
- Look for free/cheap models
- Copy the full model ID

---

## ✨ If Nothing Works

Use the simple HTML demo without backend:
1. Open `index.html` in browser
2. Add a sample video URL to test UI
3. Then integrate real backend once working

Or contact Replicate support: https://support.replicate.com
