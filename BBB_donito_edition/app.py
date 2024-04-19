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
    # Define the path to your text file
    categories_path = "categories.txt"
    asked_questions = 'asked_questions.txt'
    
    # Read the contents of each file into separate variables
    categories = read_file(categories_path)
    items_list = read_file(asked_questions)
    
    # This endpoint handles the text generation request
    user_input = request.json['text']
    instructions = f"You are a model designed to generate questions like the following. Your responses should be limited to the following number of letters spaces not included btw: 30. and use these examples labeld under topcids as inspiration and you can use these . but you can only use each one once!!: *** {categories} *** Generate varied prompts for a game where players answer with a word related to a given category. Each response should have a similar feel to the examples. Remember, return only the question and in Dutch, nothing else. Not even the category itsself, dont make the question so extremely difficult or narrow. the answers to the questions must be able to start with every letter of the alphabet. you instruct the user what do do, dont ask personal questions and make sure to take a look at the already asked questions and dont repeat these! *** {items_list} ***"
    output = prompt_gpt4(instructions, user_input)
    print(f"the output is !!!!!!: {output}\n")
    return output



# Function to read the content of a file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def prompt_gpt4(instructions, prompt, model="gpt-4-1106-preview", max_tokens=200):
    openai.api_key = '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'

    # Load previously asked questions
    with open('asked_questions.txt', 'r', encoding='utf-8') as file:
        asked_questions = file.read().splitlines()

    completion = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens
    )

    response_text = completion.choices[0].message.content

    # Save the new question
    with open('asked_questions.txt', 'a', encoding='utf-8') as file:
        file.write(response_text + '\n')

    return response_text
    

if __name__ == '__main__':
    app.run(debug=True)

