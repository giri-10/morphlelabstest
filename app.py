from flask import Flask
import os
from datetime import datetime
import subprocess
import getpass  # Import the getpass module

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Giridharan"
    username = getpass.getuser() 
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.getoutput('top -b -n 1')

    return f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {current_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)