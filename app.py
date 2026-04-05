from flask import Flask, render_template
import agent

app = Flask(__name__)

@app.route('/')
def index():
    # You can run your python logic here and pass data to the template
    script_output = "Hello from the Flask server!"
    return render_template('index.html', output=script_output)

@app.route('/hello')
def hello():   
    script_output = agent.say_hello()
    return render_template('index.html', output=script_output)

@app.route('/chat')
def chat():
    script_output = agent.chat()
    return render_template('index.html', output=script_output)
    
if __name__ == '__main__':
    app.run(debug=True)
