from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Mock user credentials (for demo purposes)
VALID_USERNAME = "Testuser"
VALID_PASSWORD = "test123"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return redirect(url_for('home'))
    else:
        return render_template('index.html', message='Invalid credentials. Please try again.')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)