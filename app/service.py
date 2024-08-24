from .models import db, User, Task

def create_user(username):
    user = User(username=username)
    db.session.add(user)
    db.session.commit()

def create_task(user_id, description):
    task = Task(descripcion=description, user_id=user_id)
    db.session.add(task)
    db.session.commit()

def mark_task_as_done(task_id):
    task = Task.query.get(task_id)
    if task:
        task.estado = 'terminada'
        db.session.commit()
