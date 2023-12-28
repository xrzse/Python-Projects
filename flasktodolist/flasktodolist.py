from flask import Flask, render_template, request

app = Flask(__name__)
tasks = []

@app.route("/", methods=['GET', 'POST'])
def todolisthome():
    if request.method == 'POST':
        task_input = request.form['task_input']
        tasks.append(task_input)
        return render_template('todolisthome.html', tasks=tasks)
    return render_template('todolisthome.html')

if __name__ == '__main__':
    app.run(debug=True)
