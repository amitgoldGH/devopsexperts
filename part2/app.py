from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def home():
    config_message = os.getenv("CONFIG_MESSAGE", "Welcome to flask")
    api_key = os.getenv("API_KEY", "No API Key")
    return f"{config_message} - API Key: {api_key}"
    
@app.route("/health/live")
def liveness():
    return "I'm alive!"
    
@app.route("/health/ready")
def readiness():
    return "I'm ready!"
    
    
app.run(host="0.0.0.0", port=5000)