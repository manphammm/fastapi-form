from pydantic import BaseModel
from typing import  Optional
from json import load, dumps
'''def read_all_user():
    with open("./data/users.json", "r") as stream:
        data_user = load(stream)
    #print(type(data_user)
    print(type(data_user))
    return data_user

print(type(read_all_user()))

#/Users/manpham/new_environmment/project/hahaha/data/users.json

test = [
    {
      "id": 1,
      "name": "Márcio",
      "mail": "example@mail.com",
      "phone": "98769878"
    },
    {
      "id": 2,
      "name": "Leandro",
      "mail": "example_leandro@mail.com",
      "phone": "94435676"
    }
  ]


'''
class User(BaseModel):
    id: int
    name: str
    mail: Optional[str] 
    phone: Optional[str]

us = User(id=10, name="nameww", mail = "mainnfn", phone ="129732")

def create_user(user: User):
    with open("./data/users.json", 'r') as new_user:
        data = load(new_user)
    dict_u = user.dict()
    data.append(dict_u)
    data = dumps(data)
    with open("./data/users.json", 'w') as new_user:
        new_user.write(data)

    return user.id
create_user(us)
