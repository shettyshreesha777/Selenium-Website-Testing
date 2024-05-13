
import os
from flask import Flask, request,jsonify
from flask_cors import CORS
import webbrowser
from pymongo import MongoClient
from streamlit.web import cli as stcli
import sys
import subprocess

app = Flask(__name__)

@app.route('/run-script-testLog', methods=['GET'])
def MongoLog():
    quantum_path= 'mongotables.py'

    subprocess.run(['python',quantum_path])
    print("Test successful")
    return "success"


@app.route('/run-script1', methods=['GET'])
def run_streamlitform():
    subprocess.run(["python", "-m", "streamlit", "run",'c:\\xampp\\htdocs\\Selenium Website Testing\\testscript_uploads\\streamlitform.py'])
    return 'Executed streamlitform.py!'


@app.route('/run-script2', methods=['GET'])
def run_streamlitLoginTC():
    subprocess.run(["python", "-m", "streamlit", "run",'c:\\xampp\\htdocs\\Selenium Website Testing\\testscript_uploads\\streamlitLoginTC.py'])
    return 'Executed streamlitLoginTC.py!'


@app.route('/run-script3', methods=['GET'])
def run_test_sport():
    subprocess.run(['python','c:\\xampp\\htdocs\\Selenium Website Testing\\testscript_uploads\\test_sport.py'])
    return 'Executed test_sport.py!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)

