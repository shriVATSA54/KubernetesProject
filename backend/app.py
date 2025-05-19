from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

feedback_list = []

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit_feedback():
    name = request.form.get('name') or "Anonymous"
    message = request.form.get('message')
    if message:
        feedback_list.append({'name': name, 'message': message})
    return redirect(url_for('home'))

@app.route('/feedback')
def show_feedback():
    return render_template("feedback.html", feedback=feedback_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
