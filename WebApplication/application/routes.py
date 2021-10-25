from application import app, db
from application.models import Tasks
from flask import render_template, url_for
from flask import redirect, request
from application.forms import AddTask

@app.route('/', methods=['GET','POST'])

@app.route('/home', methods=['GET','POST'])
def home():
    all_tasks = Tasks.query.all()
    print(all_tasks)
    return render_template('home.html',  title="Home", all_tasks=all_tasks)

@app.route('/addtask', methods=['GET', 'POST'])
def addtask():
    form = AddTask()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_task = Tasks(
                task_title = form.task_title.data,
                desc = form.desc.data,
                deadline = form.deadline.data,
                module = form.module.data,
                complete = form.complete.data
            )

            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template('addtask.html', title="Add a Task", form=form)