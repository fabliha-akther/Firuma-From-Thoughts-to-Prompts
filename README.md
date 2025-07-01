# Firuma: From Thoughts to Prompts

**Firuma** is a fun, experimental project that generates dynamic prompts based on user input in various tones—formal, poetic, funny, minimalist, and more. Currently in an early prototype stage, it explores natural language processing through interactive prompt generation, without yet integrating any large language models (LLMs). It’s built with Streamlit and designed for quick experimentation with tone-aware prompt construction. Future updates aim to incorporate LLMs and more advanced tone and context detection.

---

## Features

-  Interactive prompt generation based on user input  
-  Tone-aware suggestion system (funny, poetic, minimalist, etc.)  
-  Sentiment-driven tone adjustment via TextBlob  
-  Five prompt variants generated per input  
-  Feedback capture for quality improvement  
-  Sidebar with history of recent interactions  

---

## Tech Stack

- **Frontend/UI:** Streamlit  
- **NLP Tools:** TextBlob, NLTK  
- **Local LLM (future):** GPT4All  
- **Utilities/Data:** pandas, matplotlib, seaborn, scikit-learn  

---

## Installation Guide

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/firuma.git
   cd firuma
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

---

##  File Overview

```
├── app.py                # Main Streamlit application
├── prompt_templates.py   # Core logic for generating prompts per tone
├── tone_presets.py       # Tone styles and definitions
├── gpt_runner.py         # (Planned) Local GPT4All integration
├── requirements.txt      # Required Python packages
└── README.md             # This file
```

---

##  Demo

[Watch the demo video](https://github.com/fabliha-akther/Firuma-From-Thoughts-to-Prompts/blob/main/demo.webm)


---

## Future Plans

-  Integrate GPT4All-based response generation (`gpt_runner.py`)  
-  Add image and code category detection from natural input  
-  Replace basic sentiment detection with transformer-based classifiers  
-  Track tone usage and feedback stats over time  

---

## 📄 requirements.txt

```
streamlit
textblob
nltk
scikit-learn
seaborn
matplotlib
pandas
gpt4all
```

---

## 👤 Author

Fabliha Akther Fairuz


