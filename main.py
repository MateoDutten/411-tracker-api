import hug
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.goals import Goals
from datetime import date

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
def goal(name: hug.types.text, timeframe: hug.types.text):
    session = connect_to_db()

    goal = Goals(name=name, timeframe=date.fromisoformat(timeframe))
    session.add(goal)
    session.flush()
    session.commit()

    return "Goal created"


@hug.get()
def goal(timeframe: hug.types.text):
    with open('goals.txt', 'r') as file:
        file_content = file.read()
        # convert to json from csv
        file_content = file_content.replace("\n", ",")
        file_content = file_content[:-1]
        file_content = file_content.split(",")
        json = []
        for i in range(0, len(file_content), 3):
            if file_content[i + 1] == timeframe:
                json.append({"goal": file_content[i], "timeframe": file_content[i + 1], "date": file_content[i + 2]})
        return json
