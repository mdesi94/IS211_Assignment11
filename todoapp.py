from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)
todo_list = []


@app.route('/')
def home():
    return render_template('base.html', todo_list=todo_list)


@app.route('/submit', methods=['POST'])
def submit_task():
    global todo_list
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    item = {task, email, priority}

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return redirect('/')
    elif not task:
        return redirect('/')
    elif priority == 'Priority':
        return redirect('/')

    todo_list.append(item)
    print(todo_list)

    return redirect('/')


@app.route('/clear', methods=['POST'])
def delete():
    global todo_list
    todo_list = []

    return redirect('/clear')


if __name__ == '__main__':
    app.run()