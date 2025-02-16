from src.task import add_expense, list_expense, delete_expense, summary

def add_command(args):
    add_expense(args)

def list_command(args):
    print(list_expense(args))

def delete_command(args):
    print(delete_expense(args))

def summary_command(args):
    print(summary(args))
