import os
import json
from datetime import datetime

def make_json_file():
    if not os.path.exists('data/task.json'):
        dir_name = "data/"
        file_name = "task.json"
        task_path = os.path.join(dir_name, file_name)
        budget_path = os.path.join(dir_name, "budget.json")
        
        os.makedirs(dir_name, exist_ok=True)

        with open(task_path, 'w') as file:
            json.dump([], file)

        with open(budget_path, 'w') as file:
            json.dump({}, file)

def read_json_file(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)
    
def budget(args):
    budget = {
        "date": datetime.now().strftime("%B"),
        'date_num': datetime.now().strftime("%m"),
        "amount": format(args.amount, '.2f'),
        "used": 0
    }
    with open('data/budget.json', 'w') as file:
        json.dump(budget, file, indent=4)

    return f'A budget of {budget['amount']} has been set for {budget['date']}'

def add_expense(args):
    json_file = read_json_file('data/task.json')
    budget_file = read_json_file('data/budget.json')

    if args.amount > 0:
        expense = {
            "description": args.description,
            "category": args.category,
            "amount": f'{args.amount:.2f}',
            "id": get_id(json_file),
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        json_file.append(expense)

        with open('data/task.json', 'w') as file:
            json.dump(json_file, file, indent=4)
        
        if budget_file:
            if float(budget_file['amount']) and float(budget_file['amount']) > 0:
                new_budget = {
                    "date": datetime.now().strftime("%B"),
                    "date_num": budget_file['date_num'],
                    "amount": budget_file['amount'],
                    "used": sum(float(entry['amount']) for entry in json_file if entry['date'][5:7] == budget_file['date_num'])
                }

                if new_budget['used'] > float(new_budget['amount']):
                    print(f'The monthly budget of {budget_file['amount']} has been exceeded by ${format(float(new_budget['used']) - float(new_budget['amount']), '.2f')}')

                with open('data/budget.json', 'w') as file:
                    json.dump(new_budget, file, indent=4)
        
        return f'{expense['description']} added successfuly (ID: {expense['id']}) '

    return 'Amount must be a positive number'    

def get_id(json_file):
    return max(item['id'] for item in json_file) + 1 if len(json_file) else 1

def list_expense(args):
    json_file = read_json_file('data/task.json')

    headers = ["ID", "Date", "Description", "Category", "Amount"]

    print("{: <5} {: <10} {: <30} {: <15} {: <10}".format(*headers))
    print("-" * 70)
    for file in json_file:
        print("{: <5} {: <10} {: <30} {: <15} ${: <10}".format(str(file['id']), file['date'], file['description'], file['category'], file['amount']))

    return

def delete_expense(args):
    json_file = read_json_file('data/task.json')
    budget_file = read_json_file('data/budget.json')

    remaining_expenses = []

    for file in json_file:
        if file['id'] == args.id:
            print(f'ID: {file['id']} has been removed')
            continue
        remaining_expenses.append(file)

    new_budget = {
        "date": datetime.now().strftime("%B"),
        "date_num": budget_file['date_num'],
        "amount": budget_file['amount'],
        "used": sum(float(entry['amount']) for entry in remaining_expenses if entry['date'][5:7] == budget_file['date_num'])
                }
    
    with open('data/budget.json', 'w') as file:
        json.dump(new_budget, file, indent=4)

    with open('data/task.json', 'w') as file:
        json.dump(remaining_expenses, file, indent=4)

def summary(args):
    json_file = read_json_file('data/task.json')

    total = 0
    for file in json_file:
        if args.month and int(file['date'][5:7]) == args.month:    
            total += float(file['amount'])
        if not args.month:
            total += float(file['amount'])
        
    return f'Total expenses: ${total:.2f}' if total > 0 else 'No expenses match your request'

