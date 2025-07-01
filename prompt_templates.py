import random
from tone_presets import tone_styles  # Importing the tone styles from tone_presets.py

def get_prompt(user_input, tone_choice):
    """
    Takes the user input and selected tone and returns a detailed and varied prompt.
    The prompts are redefined to provide more elaborate responses from shorter inputs.
    """

    tone_description = tone_styles.get(tone_choice, tone_styles["default"])

    # Define Categories
    categories = {
        "text": {
            "default": [
                "Provide a formal summary of {0}, including a brief introduction, main findings, and a concluding remark, suitable for a professional audience.",
                "Compose a concise, business-style memo about {0}, detailing the key points that need to be addressed in a formal setting.",
                "Draft a formal introduction to the topic: {0}, ensuring clear structure, relevance, and no unnecessary fluff.",
                "Provide an objective overview of {0}, focusing on the key facts, data, and insights that outline its importance.",
                "Summarize the main points about {0}, giving a well-rounded view with emphasis on clarity and succinctness."
            ],
            "poetic": [
                "Write a poetic piece about {0}, using vivid imagery and metaphors to evoke deep emotions and sensory experiences.",
                "Describe {0} as if it were a dream, blending poetic language and emotional depth to highlight its beauty and significance.",
                "Write a short poem about {0}, evoking feelings of nostalgia and longing, with metaphors that connect it to nature or the passage of time.",
                "Create a lyrical description of {0}, using rich metaphors, colors, and sensory detail to paint a vivid picture in the reader's mind.",
                "Write a heartfelt piece about {0}, full of emotion and beauty, capturing its essence through tender and thoughtful verse."
            ],
            "funny": [
                "Write a funny story about {0}, making it light-hearted and humorous, with exaggerated characters and comical scenarios.",
                "Describe {0} in a humorous way, adding exaggerated traits or situations that poke fun at its most obvious features.",
                "Write a funny dialogue between two characters discussing {0}, filled with witty remarks and playful banter.",
                "Create a humorous short story about {0}, with a surprise twist at the end that leaves the reader laughing.",
                "Write a comical description of {0}, adding absurd and exaggerated details, followed by a punchline that surprises the reader."
            ],
            "minimalist": [
                "Write a concise description of {0}, capturing only the essential details in as few words as possible while maintaining clarity.",
                "Describe {0} in as few words as possible, focusing solely on the most important aspects and removing unnecessary elaboration.",
                "Write a simple, minimalist story about {0}, focusing on just the key idea without additional backstory or embellishments.",
                "Create a short, impactful description of {0}, keeping it direct and clear, with minimal words but strong meaning.",
                "Write a brief, sharp story about {0}, zeroing in on the core idea and avoiding any distractions."
            ]
        },
        "image": {
            "poetic": [
                "Create an image of {0}, evoking mystery and beauty with soft lighting, ethereal elements, and a dreamy atmosphere that transports the viewer.",
                "Generate an image of {0}, surrounded by mist and glowing lights, creating a surreal atmosphere that hints at fantasy or the unknown.",
                "Design an image of {0} at dusk, with the fading sunlight casting a mystical aura over the landscape, highlighting the transition between day and night.",
                "Create a peaceful landscape of {0}, where the beauty of nature is portrayed with delicate brush strokes and soft, flowing colors.",
                "Generate an image of {0}, full of rich, dreamlike qualities, resembling a painting with vibrant, blending hues and soft textures."
            ],
            "funny": [
                "Create an image of {0} in a humorous, exaggerated way, with playful details that make it lighthearted and comical.",
                "Design an image of {0}, with cartoonish elements and a funny twist that adds humor to the scene.",
                "Create a light-hearted image of {0} in a comical setting, where the situation is absurd and the characters are amusing.",
                "Generate an image of {0} as if it were a humorous cartoon, filled with exaggerated proportions and comedic features.",
                "Design a funny, exaggerated scene of {0}, where the characters and environment provide humorous details that make the viewer smile."
            ],
            "minimalist": [
                "Generate a minimalist image of {0}, focusing on clean lines, simplicity, and the essential elements that make it visually striking.",
                "Create a simple, elegant image of {0}, using clear shapes and minimal detail to emphasize the main subject.",
                "Design an image of {0} with a minimalist approach, stripping away all but the most essential visual elements to create a clean, impactful scene.",
                "Create an image of {0}, focusing on simplicity and negative space, with the subject standing out against a sparse background.",
                "Design a minimalist version of {0}, with few details but a strong visual impact that emphasizes the core message."
            ]
        },
        "code": {
            "poetic": [
                "Write a Python function that generates random poetry related to {0}, incorporating words like 'forest,' 'sunset,' and 'dream' to create evocative lines of verse.",
                "Create a Python script that generates poems about {0} based on user inputs, with a poetic structure and metaphorical language.",
                "Write a program that generates random poetic descriptions of {0} using metaphors, imagery, and themes of nature and beauty.",
                "Design a function that takes {0} as input and generates a poetic line or verse based on its meaning, integrating metaphor and symbolism.",
                "Create a Python script that generates random poetry about {0}, inspired by the natural world and emotional resonance."
            ],
            "funny": [
                "Write a Python script that tells random jokes about {0}, with a chatbot response that adds humor to the conversation.",
                "Create a Python function that generates funny descriptions of {0} in a humorous tone, making the process light-hearted and playful.",
                "Write a program that generates funny quotes about {0} in a chatbot style, with responses that make users laugh.",
                "Design a Python script that creates humorous responses about {0}, using keywords to generate comical outputs based on user input.",
                "Create a Python script that turns random jokes about {0} into chatbot replies, adding humor and wit to the interaction."
            ],
            "minimalist": [
                "Write a Python script that sorts a list of {0} in ascending order, with a focus on simplicity and efficient code.",
                "Create a minimalist Python program that takes {0} as input and outputs it in a simple format, ensuring readability and clarity.",
                "Write a Python function that performs basic arithmetic operations on {0}, with the logic kept concise and the output minimal.",
                "Design a Python script that reads a list of {0} and prints it in a minimalist style, focusing on clarity and brevity.",
                "Create a Python function that returns the sum of {0} values, ensuring the code is straightforward and clean."
            ]
        }
    }

    # Check category based on user input (image, code, or text)
    category = "text"  # Default category, you can dynamically set this based on user input
    if "image" in user_input.lower():
        category = "image"
    elif "code" in user_input.lower():
        category = "code"
    
    # Ensure tone_choice is valid, fallback to "default" if not found
    if tone_choice not in tone_styles:
        tone_choice = "default"

    # Select a prompt from the category and tone
    prompt = random.choice(categories[category].get(tone_choice, categories[category]["default"]))

    # Fill in the prompt with user input
    return prompt.format(user_input)
