from flask import Flask, request
from google import genai

client = genai.Client(api_key='AIzaSyCPYaEWF2N5S9dCDu1JDJND7s7moIZPWxs')

app = Flask(__name__)

@app.route("/")
def home():
    return "OK"
    
@app.route("/chat", methods=["POST"])
def chat():
    return client.models.generate_content(
        model="gemini-2.5-flash",
        contents=request.json["msg"]
    ).text

if __name__ == "__main__":
    app.run(debug=True,  port=5002)