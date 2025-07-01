import streamlit as st
import random
from tone_presets import tone_styles
from textblob import TextBlob

# Initialization
if "interactions" not in st.session_state:
    st.session_state.interactions = [{
        "input": "",
        "tone": "default",
        "prompt_options": [],
        "feedback": None,
        "submitted": False
    }]

# Utility Functions
def analyze_sentiment(user_input):
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    return "neutral"

def adjust_tone(user_input, tone):
    sentiment = analyze_sentiment(user_input)
    if sentiment == "positive":
        return "funny"
    elif sentiment == "negative":
        return "poetic"
    return tone

def generate_prompt_options(user_input):
    categories = {
        "text": [
            "Write a formal summary of {0}.",
            "Compose a concise business memo about {0}.",
            "Write a brief story about {0}."
        ],
        "image": [
            "Create an image of {0}.",
            "Generate an image of {0} in a surreal style.",
            "Design an image of {0} with minimalistic details."
        ],
        "code": [
            "Write a Python script for {0}.",
            "Create a function in Python for {0}.",
            "Design a basic code to handle {0}."
        ]
    }
    category = "text"
    base = [p.format(user_input) for p in categories[category]]
    while len(base) < 5:
        base.append(random.choice(base))
    return base

# Title & Description
st.title("Firuma: From Thoughts to Prompts")
st.write("Welcome to Firuma! Let's turn your ideas into clear, creative prompts!")

# Loop Over All Interactions 
for i, interaction in enumerate(st.session_state.interactions):
    is_latest = (i == len(st.session_state.interactions) - 1)
    with st.container():
        if not interaction["submitted"] and is_latest:
            tone_list = ["default"] + list(tone_styles.keys())

            input_value = st.text_area(
                "What would you like to say?",
                value=interaction["input"],
                key=f"input_{i}",
                height=100
            )
            st.session_state.interactions[i]["input"] = input_value

            tone_index = tone_list.index(interaction["tone"])
            tone_value = st.selectbox(
                "Choose a tone",
                tone_list,
                index=tone_index,
                key=f"tone_{i}"
            )
            st.session_state.interactions[i]["tone"] = tone_value

            if st.button("Generate Prompt", key=f"button_{i}"):
                user_input = st.session_state.interactions[i]["input"].strip()
                if user_input:
                    final_tone = adjust_tone(user_input, st.session_state.interactions[i]["tone"])
                    prompts = generate_prompt_options(user_input)
                    st.session_state.interactions[i]["tone"] = final_tone
                    st.session_state.interactions[i]["prompt_options"] = prompts
                    st.session_state.interactions[i]["submitted"] = True
        else:

            st.markdown(f"**You said:** {interaction['input']}")
            st.markdown(f"**Tone Used:** {interaction['tone']}")
            st.write("Here are your 5 prompt options:")
            for idx, prompt in enumerate(interaction["prompt_options"]):
                st.write(f"Option {idx + 1}: {prompt}")

            if interaction["feedback"] is None and is_latest:
                feedback = st.radio(
                    "Do you like this prompt?",
                    options=["Select an option", "👍", "👎"],
                    key=f"feedback_radio_{i}"
                )
                if feedback in ["👍", "👎"]:
                    st.session_state.interactions[i]["feedback"] = feedback
                    if feedback == "👍":
                        st.success("Thank you for your feedback! I'm glad you liked the prompt.")
                    else:
                        st.warning("Sorry to hear that. Feel free to try again or refine your input.")

                    st.session_state.interactions.append({
                        "input": "",
                        "tone": "default",
                        "prompt_options": [],
                        "feedback": None,
                        "submitted": False
                    })
            elif interaction["feedback"] is not None:
                st.markdown(f"**Feedback Given:** {interaction['feedback']}")

# Sidebar History 
st.sidebar.header("Chat History: ")
history_entries = [
    entry for entry in st.session_state.interactions if entry["submitted"]
][-5:]

for entry in reversed(history_entries):
    st.sidebar.write(f"Input: {entry['input']}")
    st.sidebar.write(f"Prompt: {entry['prompt_options'][0]}")
    st.sidebar.write(f"Tone: {entry['tone']}")
    st.sidebar.write(f"Feedback: {entry['feedback'] or 'Not Given'}")
    st.sidebar.write("---")
