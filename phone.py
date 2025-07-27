
# Accesing the url through ur phone
# Step-by-step:
# Find your laptop’s IP address:

# On Windows: open Command Prompt and run:
# ipconfig
# Look under your Wi-Fi section for something like: IPv4 Address: 192.168.1.7

# Run Flask like this:
# In your Python file or terminal:
# app.run(host='0.0.0.0', port=5000, debug=True)
# This makes the server visible to all devices on the network, not just localhost.

# On your phone, open a browser and go to:

# cpp
# Copy
# Edit
# http://192.168.1.7:5000
# (Replace with your actual IP from step 1.)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello Akash"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
