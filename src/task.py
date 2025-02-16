import argparse
import os
import json

def make_json_file():
    if not os.path.exists('data/task.json'):
        dir_name = "data/"
        file_name = "task.json"
        full_path = os.path.join(dir_name, file_name)
        
        os.makedirs(dir_name, exist_ok=True)

        with open(full_path, 'w') as file:
            json.dump([], file)

def read_json_file():
    with open('data/task.json', 'r') as file:
        return json.load(file)

def add_expense(args):
    json_file = read_json_file()

    expense = {
        "description": args.description,
        "category": args.category,
        "amount": f'{args.amount:.2f}',
        "id": get_id(json_file)
    }

    json_file.append(expense)

    with open('data/task.json', 'w') as file:
        json.dump(json_file, file, indent=4)
    
    print(f'{expense['description']} added to tracker')

def get_id(json_file):
    return max(item['id'] for item in json_file) + 1 if len(json_file) else 1

def list_expense(args):
    return args

def delete_expense(args):
    return args

def summary(args):
    return args
