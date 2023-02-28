import sqlalchemy as db
import sqlalchemy.orm as orm
import model as m
import datetime

done = m.Status(name='Done')
pending = m.Status(name='Pending')

task = m.Task(date=datetime.date.today(), subject='Get code working')
task.status = pending

home = m.Tag(name='Home')
work = m.Tag(name='Work')

task.tags = [home, work]

engine = db.create_engine('sqlite:///todo.sqlite', echo=False)

with orm.Session(engine) as session:
    session.add(done)
    session.add(pending)

    session.add(task)
    session.add(
        m.Task(date=datetime.date.fromisoformat('2023-03-02'),
               subject='Get started on library task')
    )

    print(task)
    print(pending.tasks)

    tasks = session.query(m.Task).all()

    for task in tasks:
        print(task)

    session.commit()
