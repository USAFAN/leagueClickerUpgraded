from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <body>
                <button onclick="window.location.href='/playpause'">Play/Pause</button>
            </body>
        </html>
    '''

@app.route('/playpause')
def playpause():
    # Use subprocess to execute a command that emulates the play/pause button on your local home Wi-Fi
    subprocess.run(["command", "to", "play/pause", "button"])
    return "Success!"

if __name__ == '__main__':
    app.run()
