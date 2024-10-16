import hug
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.goals import Goals
from datetime import date
from sqlalchemy import delete

@hug.response_middleware()
def process_data(request, response, resource):
    response.set_header('Access-Control-Allow-Origin', '*')
    response.set_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    response.set_header('Access-Control-Allow-Headers', 'Content-Type')


def connect_to_db():
    engine = create_engine('sqlite:///411-tracker-api.sqlite')
    conn = engine.connect()
    return Session(conn)

@hug.post()
def goal(name: hug.types.text, timeframe: hug.types.text, start_date: hug.types.text):
    session = connect_to_db()
    goal = Goals(name=name, timeframe=timeframe, start_date=date.fromisoformat(start_date))
    session.add(goal)
    session.flush()
    session.commit()

    return "Goal created"

@hug.delete()
def goal(goal_id: hug.types.text):
    session = connect_to_db()
    goal = (delete(Goals).where(Goals.id == goal_id))
    session.execute(goal)
    return "Goal Deleted"


@hug.get()
def goal(timeframe: hug.types.text):
    session = connect_to_db()
    goals = session.query(Goals).filter(Goals.timeframe == timeframe).all()
    return [{'date': goal.start_date, 'goal': goal.name, 'timeframe': goal.timeframe} for goal in goals]

@hug.get()
def get_id():
    session = connect_to_db()
    goals = session.query(Goals).filter(Goals.id).all()
    return [{'id': goal.id} for goal in goals]