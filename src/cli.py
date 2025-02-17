import argparse
from src.commands import add_command, list_command, summary_command, delete_command

def setup_parser():
    parser = argparse.ArgumentParser(
        prog="Expense Tracker CLI",
        description="CLI tool to add, update, delete, and track expenses"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="add expense to record")
    add_parser.add_argument("-d", "--description", required=True, type=str, help="description of expense")
    add_parser.add_argument("-c", "--category", type=str, required=True, help="categorize the expense")
    add_parser.add_argument("-a", "--amount", type=float, required=True, help="dollar amount of expense added")
    add_parser.set_defaults(func=add_command)

    list_parser = subparsers.add_parser("list", help="list expenses")
    list_parser.add_argument("-l", "--limit", type=int, help="limit the number of records retrieved")
    list_parser.add_argument("-c", "--category", type=str, help="retrieve list of an individual category")
    list_parser.set_defaults(func=list_command)

    summary_parser = subparsers.add_parser("summary", help="retrieves total expenses")
    summary_parser.add_argument("-m", "--month", type=int, help="retrieve summary of a particular month")
    summary_parser.set_defaults(func=summary_command)

    delete_parser = subparsers.add_parser("delete", help="delete expense")
    delete_parser.add_argument("--id", type=int, required=True, help="ID of record to delete")
    delete_parser.set_defaults(func=delete_command)

    return parser
