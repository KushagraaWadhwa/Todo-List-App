from flask import Flask, render_template, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class TodoKW(db.Model):
    t_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    complete = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return f"{self.t_id} - {self.title}"


@app.route('/', methods=['GET','POST'])
def welcome():
    if request.method=='POST' and "username" in request.form:
        username = request.form["username"]
        return redirect("/dash?username="+username)

    return render_template('login.html')


@app.route('/taskform', methods=['GET','POST'])
def form():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        task = TodoKW(title=title, desc=desc, complete=False)
        db.session.add(task)
        db.session.commit()
        
    alltodoKW = TodoKW.query.all()
    return render_template('taskform.html', alltodoKW=alltodoKW)
    

@app.route('/dash', methods=['GET','POST'])
def dashboard():
    if request.method=="GET":
        args = request.args
        username=args.get('username')
        return render_template('dashboard.html',username=username)
    else:
        username=""
    
    return render_template('dashboard.html',username=username)

@app.route('/summary', methods=['GET','POST'])
def summary():
    total_todo = TodoKW.query.count()
    completed_todo = TodoKW.query.filter_by(complete=True).count()
    not_completed_todo = total_todo-completed_todo
    return render_template('summary.html',total_todo=total_todo, completed_todo=completed_todo, not_completed_todo=not_completed_todo)
 

#---------------------------API's Update/Delete/Check Progress-------------------------------------------------
@app.route('/delete/<int:t_id>')
def delete(t_id):
    task = TodoKW.query.filter_by(t_id=t_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect("/taskform")

@app.route('/update/<int:t_id>', methods=['GET', 'POST'])
def update(t_id):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        task = TodoKW.query.filter_by(t_id=t_id).first()
        task.title = title
        task.desc = desc
        db.session.add(task)
        db.session.commit()
        return redirect("/taskform")
        
    task = TodoKW.query.filter_by(t_id=t_id).first()
    return render_template('update.html', task=task)

@app.route('/progress/<int:t_id>')
def progress(t_id):
    todo = TodoKW.query.filter_by(t_id=t_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for('form'))
        



if __name__ == "__main__":
    app.run(debug=True, port=8000)