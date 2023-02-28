import sqlalchemy as db
import sqlalchemy.orm as orm

# import sqlalchemy.ext.declarative as base

# This is the abstract base class

Base = orm.declarative_base()


# Statuses

class Status(Base):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

    def __repr__(self):
        return self.name

# Tasks

class Task(Base):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DATE)
    subject = db.Column(db.String)
    status_id = db.Column(
        db.Integer,
        db.ForeignKey('status.id')
    )

    status = orm.relationship('Status', backref='tasks')

    tags = orm.relationship('Tag',
                            secondary='task_tag',
                            back_populates='tasks')

    def __repr__(self):
        return f'{self.date} - {self.subject} - {self.status} - {self.tags}'

# Link tasks to tags

task_tag = db.Table(
    'task_tag',
    Base.metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('task_id', db.ForeignKey('task.id')),
    db.Column('tag_id', db.ForeignKey('tag.id')),
    db.UniqueConstraint('task_id', 'tag_id')

)

# Tags

class Tag(Base):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

    tasks = orm.relationship('Task',
                            secondary='task_tag',
                            back_populates='tags')

    def __repr__(self):
        return self.name