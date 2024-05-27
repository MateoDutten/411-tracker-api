import hug


@hug.response_middleware()
def process_data(request, response, resource):
    response.set_header('Access-Control-Allow-Origin', '*')
    response.set_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    response.set_header('Access-Control-Allow-Headers', 'Content-Type')


@hug.post()
def goal(goal: hug.types.text, timeframe: hug.types.text,  date: hug.types.text):
    with open('goals.txt', 'a') as file:
        file.write(goal + "," + timeframe + "," + date + "\n")
    return "Goal created"


@hug.get()
def goal(timeframe: hug.types.text):
    with open('goals.txt', 'r') as file:
        file_content = file.read()
        # convert to json from csv
        file_content = file_content.replace("\n", ",")
        file_content = file_content[:-1]
        file_content = file_content.split(",")
        print(file_content)
        json = []
        for i in range(0, len(file_content), 3):
            if file_content[i+1] == timeframe:
                json.append({"goal": file_content[i], "timeframe": file_content[i+1], "date": file_content[i+2]})
        return json
