from rich import box
from rich.console import Console
from rich.table import Table
from db import SessionLocal
from habit import Habit

console = Console()


def add(name, description=""):
    "Add a new habit"
    session = SessionLocal()
    habit = Habit(name=name, description=description)
    session.add(habit)
    session.commit()
    session.close()
    console.print(f"[green]Added habit:[/] {name}")


def list_habits():
    "List all habits"
    session = SessionLocal()
    habits = session.query(Habit).all()
    session.close()

    table = Table(title="Your Habits", box=box.ROUNDED)
    table.add_column("ID", style="cyan", justify="right")
    table.add_column("Name", style="magenta")
    table.add_column("Description", style="yellow")
    table.add_column("Completed", style="green")

    for habit in habits:
        table.add_row(str(habit.id), habit.name,
                      habit.description or "—", "Yes" if habit.completed else "No")

    console.print(table)


def complete_habit(name):
    "Mark a habit as completed"
    session = SessionLocal()
    habit = session.query(Habit).filter(Habit.name == name).first()
    if habit:
        habit.completed = True
        session.commit()
        session.close()
        console.print(f"[green]Marked habit as completed:[/] {name}")
    else:
        console.print(f"[red]Habit not found:[/] {name}")
