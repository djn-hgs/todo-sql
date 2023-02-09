import sqlalchemy as db
import model

engine = db.create_engine('sqlite:///todo.sqlite', echo=True)

model.Base.metadata.create_all(engine)
