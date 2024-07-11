import sqlalchemy as db


engine = db.create_engine('sqlite:///411-tracker-api.sqlite')
conn = engine.connect()
metadata = db.MetaData()

goals = db.Table('goals', metadata,
                 db.Column('id', db.Integer(), primary_key=True),
                 db.Column('name', db.String(255), nullable=False),
                 db.Column('timeframe', db.DateTime()),
                 )


metadata.create_all(engine)