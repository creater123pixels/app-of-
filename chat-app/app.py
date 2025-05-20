 from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

PASSWORD = "letmein123"  # The password for the chat
messages = []  # A list to store messages

# Route to access the chat
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        if password != PASSWORD:
            return "Incorrect password. Please try again.", 403

        username = request.form['username']
        message = request.form['message']
        timestamp = datetime.now().strftime('%H:%M:%S')
        messages.append({'username': username, 'message': message, 'time': timestamp})
        return redirect('/')

    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
