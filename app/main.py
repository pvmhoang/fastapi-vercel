
import os
import json
from pathlib import Path
from fastapi import FastAPI

app = FastAPI()

def read_file(file_name: str):
    with open(file_name, "r") as input_file:
         data = json.load(input_file)
         return data

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/json")
def read_json():
    # working
    current_directory = os.getcwd()
    print(current_directory)
    absolute_path = current_directory + '/app/data/master-data.json'
    return read_file(absolute_path)
    # working

    # content = Path('master-data.json').read_text()
    # print(content)
    # with open('master-data.json', 'r') as json_file:
    #     data = json_file.read()
    # return json.load()
    
    # return read_file('./data/master-data.json')
    # return read_file('master-data.json')