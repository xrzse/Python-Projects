from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def todolisthome():
    return render_template('todolisthome.html')

if __name__ == '__main__':
    app.run(debug=True)