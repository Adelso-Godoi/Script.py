from flask import Flask
import subprocess
import paramiko

app = Flask(__name__)

@app.route("/restart")
def restart():

    subprocess.run(["python3","restart.py"])

    return "OK"

app.run()