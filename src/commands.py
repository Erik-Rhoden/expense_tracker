from src.task import add_expense, list_expense, delete_expense, summary

def add_command(args):
    add_expense(args)

def list_command(args):
    list_expense(args)

def delete_command(args):
    delete_expense(args)

def summary_command(args):
    summary(args)
