import google.generativeai as genai
from flask import Flask, render_template, request

# Set your Gemini API Key
# You'll need to add your API key here
genai.configure(api_key="AIzaSyDZgG-f40-CBMFa9Akeyp2F-eZiomSQSyY")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    user_input = msg
    return get_chat_response(user_input)  # Changed from get_Chat_response to get_chat_response

def get_chat_response(text):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(text)
    return response.text

if __name__ == '__main__':
    app.run(debug=True)