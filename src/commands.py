from src.task import add_expense, list_expense, delete_expense, summary, budget

def add_command(args):
    print(add_expense(args))

def budget_command(args):
    print(budget(args))

def list_command(args):
    list_expense(args)

def delete_command(args):
    delete_expense(args)

def summary_command(args):
    print(summary(args))
