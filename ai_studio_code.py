# To run this code you need to install the following dependencies:
# pip install google-genai

import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-3-flash-preview"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""hi 
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Hello! How can I help you today?"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""You are an expert AI video creator.

Create a high-quality cinematic video based on the following details:

🎯 Topic: [ENTER TOPIC]
🎭 Genre: [funny / emotional / adventure / horror / educational]
👶 Target Audience: [kids / adults / general]
⏱ Duration: [30 sec / 1 min / etc.]

🎥 Style:
- 3D Cartoon / Pixar Style / Realistic / Anime (choose one)
- Bright, colorful, visually engaging
- Smooth camera movements
- High-quality lighting and shadows

🧍 Characters:
- Describe main character (age, look, clothes, personality)
- Add supporting characters if needed (animals, friends, etc.)

📍 Scenes:
Divide into 5–6 scenes. For each scene include:
1. Scene description (what is happening)
2. Character actions
3. Camera movement (zoom, pan, tracking, etc.)
4. Background environment
5. Mood / emotion

🎙 Voiceover:
- Simple English
- Engaging and emotional
- Match tone with story

🎵 Background Music:
- Style: [funny / magical / emotional / suspense]
- Instruments: piano / ukulele / cartoon sounds

🔊 Sound Effects:
- Add small effects (footsteps, pop, whoosh, animal sounds)

🎬 Ending:
- Add a strong ending (funny twist / lesson / surprise)

📱 Output Format:
- YouTube Shorts / TikTok / Reel (vertical 9:16)[16:9]
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""**Developing the Narrative**

I'm currently fleshing out the cinematic video script. I'm focusing on crafting a compelling narrative flow, given the placeholder details within the user-provided template. I'm aiming for a high-quality, engaging brief for the expert AI video creator.


**Generating a Sample Scenario**

I've decided to create a sample video concept to demonstrate the AI's capabilities. My plan is to use a lighthearted theme - a clumsy robot baking a cake. I've defined the topic, genre (funny), target audience (kids/general), duration (60 seconds), style (3D Pixar), and character (B0B, a round robot). I'm also planning 5-6 scenes with a voiceover and upbeat music. I'm visualizing the scenes, with the first being an introduction, then chaos!


"""),
                types.Part.from_text(text="""I am ready. To give you a taste of what I can create, I have put together a high-quality sample project using your template. 

**Once you review this, please provide your specific details, and I will generate a custom script for you!**

---

### 🎥 Project Title: \"The Great Acorn Heist\"

🎯 **Topic:** A clumsy squirrel trying to get a golden acorn.
🎭 **Genre:** Funny / Slapstick
👶 **Target Audience:** Kids / General
⏱ **Duration:** 45 Seconds

🎥 **Style:**
*   **Look:** 3D Pixar Style (High-detail fur, expressive eyes)
*   **Visuals:** Bright, saturated forest colors, golden hour lighting.
*   **Cinematography:** High-speed action shots followed by slow-motion \"fail\" moments.

🧍 **Characters:**
*   **Pip (Main):** A small, hyperactive squirrel with an oversized bushy tail and a tiny aviator hat. He is over-confident but very clumsy.
*   **The Blue Jay (Supporting):** A grumpy bird watching from a branch, acting as the \"judge.\"

📍 **Scenes:**

1.  **The Target:** 
    *   *Description:* A massive, shimmering golden acorn sits atop a thin, wobbly branch.
    *   *Actions:* Pip looks through binoculars made of two hollowed-out nuts.
    *   *Camera:* Slow zoom into Pip’s dilated pupils reflecting the acorn.
    *   *Environment:* Lush, sun-drenched autumn forest.
    *   *Mood:* Epic/Determined.

2.  **The Launch:** 
    *   *Description:* Pip prepares to jump from a neighboring tree.
    *   *Actions:* He stretches like an Olympic athlete, then launches himself with a massive \"boing.\"
    *   *Camera:* Tracking shot following Pip mid-air.
    *   *Environment:* Blurry leaves rushing past.
    *   *Mood:* High energy.

3.  **The Mid-Air Crisis:** 
    *   *Description:* A butterfly flutters past Pip's nose mid-jump.
    *   *Actions:* Pip sneezes violently, losing his aerodynamic form and spinning like a propeller.
    *   *Camera:* Slow-motion 360-degree rotation around Pip’s panicked face.
    *   *Mood:* Hilarious/Chaos.

4.  **The Impact:** 
    *   *Description:* Pip misses the branch and hits a beehive instead.
    *   *Actions:* Pip’s face squishes against the hive; his eyes go wide.
    *   *Camera:* Close-up, shaky cam.
    *   *Environment:* Deep inside the shaded leaves.
    *   *Mood:* Suspense.

5.  **The Escape:** 
    *   *Description:* Pip realizes his mistake and tries to swim through the air.
    *   *Actions:* He grabs the golden acorn at the last second as he falls.
    *   *Camera:* High-angle shot looking down as he drops.
    *   *Mood:* Panic.

🎙 **Voiceover:**
*   \"Meet Pip. He has a plan. A perfect plan. (Pip sneezes) Okay... maybe not *that* perfect. Hold on tight, Pip!\"

🎵 **Background Music:**
*   **Style:** Orchestral/Magical starting into Fast Jazz/Cartoon Chase.
*   **Instruments:** Xylophone, Tuba for the \"thuds,\" and fast violins.

🔊 **Sound Effects:**
*   *Whoosh* of the jump, *A-choo!* sneeze, *Slide-whistle* for the fall, *Buzzing* of bees.

🎬 **Ending:**
*   Pip lands safely on the ground with the acorn. He bites it, only to realize it’s a painted rock. It chips his tooth. The Blue Jay laughs in the background.

📱 **Output Format:** 9:16 (YouTube Shorts / TikTok)

---

**Now, please give me your details so I can create your custom script!**
*   **Topic:**
*   **Genre:**
*   **Target Audience:**
*   **Duration:**
*   **Style:** (3D/Realistic/Anime/etc.)"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="HIGH",
        ),
        tools=tools,
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if text := chunk.text:
            print(text, end="")

if __name__ == "__main__":
    generate()


