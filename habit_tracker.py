import click
from console import list_habits, add, complete_habit
from db import create_tables
import os


@click.group()
def cli():
    "Habit Tracker CLI"
    create_tables()


@click.command()
@click.argument("name")
@click.option("--desc", "-d", default="", help="Optional habit description")
def add_habit(name, desc):
    "Add a new habit"
    add(name, desc)


@click.command()
def listout():
    "List all habits"
    list_habits()


@click.command()
@click.argument("name")
def complete(name):
    "List all habits"
    complete_habit(name=name)


cli.add_command(add_habit, name="add")
cli.add_command(listout, name="list")
cli.add_command(complete, name="complete")

if __name__ == "__main__":
    if not os.path.exists("habit_tracker.db"):
        if os.path.exists("db.py"):
            import subprocess
            subprocess.run(["python", "db.py"])
        else:
            raise FileNotFoundError("db.py not found")
    cli()
