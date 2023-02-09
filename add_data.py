import sqlalchemy as db
import sqlalchemy.orm as orm
import model as m
import datetime

done = m.Status(name='Done')
pending = m.Status(name='Pending')

task = m.Task(date=datetime.date.today(), subject='Get code working')
another = m.Task(date=datetime.date.today(), subject='Get haircut')
task.status = pending
another.status = pending

home = m.Tag(name='Home')
work = m.Tag(name='Work')
school = m.Tag(name='School')

task.tags = [home, school]
another.tags.append(home)

engine = db.create_engine('sqlite:///todo.sqlite', echo=False)

with orm.Session(engine) as session:
    session.add(done)
    session.add(pending)

    session.add(task)


    print(task)
    print(pending.tasks)
    print(home.tasks)

    session.commit()
