from flask import Flask, request, render_template, redirect, url_for
import hashlib
import base64
import os
from utils import generate_passkey, encode_email, decode_email

app = Flask(__name__)
app.secret_key = "demo-secret-key"

# Simulated database
users = {
    "victim@example.com": {"password": "oldpass", "token": ""},
    "thegeekaman@test.com": {"password": "oldpass", "token": ""}
}

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Password Reset Demo</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <div class="container text-center mt-5">
            <h2 class="mb-4">Password Reset Demo</h2>
            <a href="/request-reset" class="btn btn-primary">Click here to reset password</a>
        </div>
    </body>
    </html>
    '''

@app.route('/request-reset', methods=['GET', 'POST'])
def request_reset():
    if request.method == 'POST':
        email = request.form['email']
        if email in users:
            passkey = generate_passkey()
            users[email]['token'] = passkey

            # Generate https reset link with properly encoded email
            encoded = encode_email(email)
            reset_link = f"http://127.0.0.1:5000/reset-password?passkey={passkey}&email={encoded}"

            return f'''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Reset Link</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
            </head>
            <body class="bg-light">
                <nav class="navbar navbar-dark bg-dark mb-4">
                    <div class="container">
                        <span class="navbar-brand mb-0 h1">Reset Demo</span>
                    </div>
                </nav>
                <div class="container mt-5">
                    <div class="row justify-content-center">
                        <div class="col-md-8">
                            <div class="card shadow p-4">
                                <h4 class="mb-3 text-success">Password Reset Link Generated</h4>
                                <p class="mb-3">Click the link below to reset your password:</p>
                                <div class="alert alert-secondary">
                                    <a href="{reset_link}" target="_blank">{reset_link}</a>
                                </div>
                                <a href="/" class="btn btn-outline-primary mt-3">Go back to Home</a>
                            </div>
                        </div>
                    </div>
                </div>
            </body>
            </html>
            '''
        return "User not found"
    return render_template('reset_request.html')

@app.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    passkey = request.args.get('passkey')
    encoded_email = request.args.get('email')
    try:
        email = decode_email(encoded_email)
    except:
        return "Invalid email encoding"

    if users.get(email) and users[email]['token'] == passkey:
        if request.method == 'POST':
            password = request.form['password']
            confirm = request.form['confirm']
            if password == confirm:
                users[email]['password'] = password
                return "Password reset successful!"
            return "Passwords do not match"
        return render_template('reset_password.html', email=encoded_email, passkey=passkey)
    return "Invalid reset link"

if __name__ == '__main__':
    app.run(debug=True)
