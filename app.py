from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('linkedin_follow.html')  # Make sure this HTML file is in the 'templates' folder

if __name__ == "__main__":
    # Run the app on the local network
    app.run(host='0.0.0.0', port=5000)
