from flask import Flask

app = Flask(__name__)



@app.route('/')
def home():
    config_message = os.getenv("CONFIG_MESSAGE", "Welcome to flask")
    api_key = os.getenv("API_KEY", "No API Key")
    return f"{welcome_message} - API Key: {api_key}"
    
@app.route("/home")
def hello_worlde():
    return "<p>Hello, Worlde!</p>"
    
    
app.run(host="0.0.0.0", port=5000)