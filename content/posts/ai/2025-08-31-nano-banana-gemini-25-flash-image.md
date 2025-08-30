---
categories: [AI, Computer Vision, Developer Tools]
cover: /img/nano-banana-cover.jpg
date: 2025-08-30
description: Nano Banana(Gemini 2.5 Flash Image)의 핵심 기능, 최신 뉴스, 가격과 접근 방법, 실전 프롬프트·API 예제까지 한 번에 정리합니다.
image: /img/nano-banana-cover.jpg
keywords: nano banana,Gemini 2.5 Flash Image,AI image editing,Google GenAI,character consistency,SynthID
layout: post
organiser: Royfactory
tags: [nano-banana, gemini, image-editing, genai, google]
title: "Nano Banana (Gemini 2.5 Flash Image): A Field Guide for Builders"
slug: nano-banana-gemini-25-flash-image
toc: true
---

## Introduction
**Nano Banana** is Google DeepMind’s codename for **Gemini 2.5 Flash Image**, a state-of-the-art model for native image **generation and editing**. It brings natural-language targeted edits, **identity consistency** across scenes, multi-image fusion, world-knowledge-guided edits, and **SynthID watermarking** to keep provenance intact. It’s available in the Gemini app and via API (AI Studio / Vertex AI). Pricing is transparent at about **$0.039 per image**. :contentReference[oaicite:29]{index=29}

## What’s New
### Identity Consistency
Keep a person, pet, or product looking like itself across variations—perfect for brand sets or episodic content. :contentReference[oaicite:30]{index=30}

### Targeted, Natural-Language Edits
Blur backgrounds, remove objects, change poses, recolor, and more—no masks or layers required. :contentReference[oaicite:31]{index=31}

### Multi-Image Fusion
Combine multiple inputs into coherent scenes for product placement, room restyling, or group photos. :contentReference[oaicite:32]{index=32}

### Watermarking & Safety
All outputs ship with visible marks and **SynthID** invisible watermarks for provenance. :contentReference[oaicite:33]{index=33}

## Latest Headlines at a Glance
- Sundar Pichai teased the launch with the “three bananas” post; the codename stuck. :contentReference[oaicite:34]{index=34}  
- LMArena shows the model topping the **Image Edit** leaderboard. :contentReference[oaicite:35]{index=35}  
- Coverage notes strengths in consistency—and community concerns around deepfakes and basic crop limitations. :contentReference[oaicite:36]{index=36}

## Quickstart (API)
### Python (google-genai)
```python
from google import genai
from PIL import Image
from io import BytesIO

client = genai.Client()
src = Image.open("input.jpg")
prompt = "Keep identity; swap background to studio lighting."

resp = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[prompt, src],
)
# Save first image part
for c in resp.candidates:
    for p in c.content.parts:
        if getattr(p, "inline_data", None):
            Image.open(BytesIO(p.inline_data.data)).save("output.jpg")
````

Inline images + text make up a **single** multimodal request; multiple images enable fusion. See official docs for language guides and Vertex AI parity. ([Google AI for Developers][9], [Google Cloud][13])

### TypeScript (@google/genai)

```ts
import { Client } from "@google/genai";
import * as fs from "node:fs";

const client = new Client({ apiKey: process.env.GEMINI_API_KEY });

const buf = fs.readFileSync("input.jpg");

const resp = await client.models.generateContent({
  model: "gemini-2.5-flash-image-preview",
  contents: [
    { inline_data: { mime_type: "image/jpeg", data: buf } },
    "Place me in a cozy cafe, keep face and outfit identical.",
  ],
});
```

## Pro Prompt Recipes

* “Keep face and hairstyle identical; replace background with a narrow Italian alley.”
* “\[Product PNG] + \[room photo] → Place product naturally on the shelf; reduce specular highlights.”
* “\[Me], \[my dog] → Sunset beach walk; both identities unchanged; realistic lighting.”

## Pricing & Access

* **\$30 per 1M output tokens (\~\$0.039 / image)**, via Developer API and Vertex AI; model is **public preview** as of Aug 26, 2025. ([Google Developers Blog][3], [Google Cloud][4])

## Risks & Responsible Use

Identity consistency is powerful but raises **deepfake** risks; keep consent, disclosure, and watermark retention in your workflow. ([PC Gamer][7])

## Conclusion

Nano Banana isn’t just a new image model—it’s a **production-ready editing pipeline** for consistent characters and brand visuals. Move fast, test in the app, then wire the API into your toolchain.

---

### Summary

* Nano Banana = Gemini 2.5 Flash Image (public preview).
* Strengths: identity consistency, precise local edits, multi-image fusion.
* Transparent pricing and API parity across AI Studio & Vertex AI.
* Built-in SynthID watermarking for provenance.
* Use responsibly; disclose edits and retain watermarks.

```

**Notice:** :contentReference[oaicite:40]{index=40}
::contentReference[oaicite:41]{index=41}
```

[1]: https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/?utm_source=chatgpt.com "Introducing Gemini 2.5 Flash Image, our state-of-the-art image model"
[2]: https://blog.google/intl/en-mena/product-updates/explore-get-answers/nano-banana-image-editing-in-gemini-just-got-a-major-upgrade/ "Nano Banana! Image editing in Gemini just got a major upgrade"
[3]: https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/ "
            
            Introducing Gemini 2.5 Flash Image, our state-of-the-art image model
            
            
            \- Google Developers Blog
            
        "
[4]: https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash?utm_source=chatgpt.com "Gemini 2.5 Flash | Generative AI on Vertex AI"
[5]: https://timesofindia.indiatimes.com/technology/tech-news/google-ceo-sundar-pichai-shares-3-bananas-heres-what-they-mean/articleshow/123548276.cms "Google CEO Sundar Pichai shares '3 Bananas’: Here’s what they mean - The Times of India"
[6]: https://lmarena.ai/leaderboard "Overview Leaderboard | LMArena"
[7]: https://www.pcgamer.com/software/ai/geminis-nano-banana-update-aims-to-keep-people-looking-the-same-in-ai-art-and-the-fear-of-deepfakes-makes-me-want-to-wear-a-brown-paper-bag-on-my-head-forever-more/ "Gemini's 'Nano Banana' AI image editor can't crop a picture, but its penchant for deepfakes 'while keeping you, you' makes me want to wear a brown paper bag on my head forever more | PC Gamer"
[8]: https://techcrunch.com/2025/08/26/google-geminis-ai-image-model-gets-a-bananas-upgrade/?utm_source=chatgpt.com "Google Gemini's AI image model gets a 'bananas' upgrade"
[9]: https://ai.google.dev/gemini-api/docs/image-generation?utm_source=chatgpt.com "Image generation with Gemini (aka Nano Banana) - Gemini API"
[10]: https://ai.google.dev/gemini-api/docs/libraries?utm_source=chatgpt.com "Gemini API libraries | Google AI for Developers"
[11]: https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstart?utm_source=chatgpt.com "Gemini API in Vertex AI quickstart"
[12]: https://developers.googleblog.com/en/how-to-prompt-gemini-2-5-flash-image-generation-for-the-best-results/?utm_source=chatgpt.com "How to prompt Gemini 2.5 Flash Image Generation ..."
[13]: https://cloud.google.com/vertex-ai/generative-ai/docs/sdks/overview?utm_source=chatgpt.com "Google Gen AI SDK | Generative AI on Vertex AI"
[14]: https://coinmarketcap.com/currencies/banano/?utm_source=chatgpt.com "Banano price today, BAN to USD live price, marketcap ..."
[15]: https://www.coingecko.com/en/coins/banano?utm_source=chatgpt.com "Banano Price: BAN Live Price Chart, Market Cap & News ..."
