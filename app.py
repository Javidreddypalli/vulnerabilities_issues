from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/run")
def run():
    cmd = request.args.get("cmd")
    os.system(cmd)  # Insecure code: command injection
    return "Done"
def example():
    print("Hello world")

example()