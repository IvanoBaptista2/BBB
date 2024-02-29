from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import openai


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    # Serves the index.html file
    return render_template('index.html')

@app.route('/generate-text', methods=['POST'])
def generate_text():
    # This endpoint handles the text generation request
    user_input = request.json['text']
    instructions = "You are a model designed to generate open ended questions where you can answer the length of one word to. Your responses should be limited to the following categories: 'food and drinks', 'science', 'nature', 'tech', 'the world','smoke topics', 'random categories', and 'entertainment'. Feel free to think of more categories if you wish! Your task is to generate a series of single-topic questions or prompts. Each response should focus on one non specific category at a time, such as 'Iets duurs', 'Iets in je lichaam', 'drinken', 'Iets dat je op vakantie kan doen', 'iets waarmee je kan gooien', 'valuta', 'Iets sportsgerelateerds', 'Iets ninendo gerelateerds', 'iets joint gerelateerds' and so on. The goal is for these prompts to be simple and direct and always be different. Feel free to explore a wide array of categories beyond the examples provided, like animals, geographical locations, historical figures, or any other area of interest. Remember, the key is to keep each prompt focused on just one item or concept return only the question and in dutch, nothing else not even the category."
    output = prompt_gpt4(instructions, user_input)
    print(f"the output is !!!!!!: {output}")
    return jsonify(output)

def prompt_gpt4(instructions, prompt, model="gpt-4-1106-preview", max_tokens=2000):
    openai.api_key = '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'

    completion = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens
    )

    response_text = completion.choices[0].message.content
    return response_text

if __name__ == '__main__':
    app.run(debug=True)

