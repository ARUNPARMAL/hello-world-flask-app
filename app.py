from flask import Flask
# from waitress import serve

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, Azure Web Apps!"

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)  
