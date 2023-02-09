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


    print(task)
    print(pending.tasks)

    session.commit()
