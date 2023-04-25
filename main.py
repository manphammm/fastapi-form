from fastapi import FastAPI
from json import load, dumps
from schema import User

app = FastAPI()

@app.get("/api")
def root():
    hello = { "API": "Hello"}
    return hello

@app.get("/api/users")
def read_all_user():
    with open("./data/users.json", "r") as stream:
        data_user = load(stream)
    #print(type(data_user)
    return data_user

@app.get("/api/question/{position}")
def find_question_position(position: int):
    with open("./data/questions.json", "r") as ques:
        data_question = load(ques)
    for iter_ques in data_question:
        if iter_ques['position'] == position:
            return iter_ques

@app.post("/api/users")
def create_user(user: User):
    with open("./data/users.json", 'r') as new_user:
        data = load(new_user)

    dict_u = user.dict()
    data.append(dict_u)
    data = dumps(data)
   
    with open("./data/users.json", 'w') as new_user:
        new_user.write(data)
    
    return user.id
    

    
