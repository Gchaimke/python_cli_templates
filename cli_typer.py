
from datetime import datetime
from tkinter.font import names
from typing import List

import click
import typer

app = typer.Typer()
cities = ["TelAviv","Reeshon","Holon","BatYam"]

class User:
    __slots__ = ["name", "birthday", "city", "date"]

    def __init__(self, **args):
        self.name = args.get("name", "")
        self.birthday = args.get("birthday", "")
        self.city = args.get("city", "")
        self.date = args.get("date", "")
        pass

    def __str__(self):
        return f"Hello {self.name} from {self.city}.\nYour birthday is: {self.birthday}.\nYou start wotking at: {self.date}\n"


def complete_city(ctx:typer.Context, incomplete: str):
    citys = ctx.params.get("city") or []
    for city in cities:
        if city.startswith(incomplete) and city not in citys:
            yield(city)

def validate_date(ctx, param, value):
    try:
        if isinstance(value, str):
            datetime.strptime(value, "%d.%m.%Y")
            return value
        else:
            for date in value:
                datetime.strptime(date, "%d.%m.%Y")
            return value
    except ValueError:
        raise click.BadParameter("Date must be in format DD.MM.YYYY")

@app.command()
def main(
    name: str = typer.Option("Chaim","--name","-n", help="Your Name",
                             prompt="Enter your name"),
    birthday: str = typer.Option(
        "10.12.1985", help="Your birthday in YYYY-MM-DD format", callback=validate_date, prompt="Enter your birthday in YYYY-MM-DD format"),
    city: List[str] = typer.Option("TelAviv", help="Your City",
                             prompt="Enter your city",autocompletion=complete_city),
    start_date: str = typer.Option(
        "04.04.2022", help="The sart date", callback=validate_date, prompt="Enter your start working day"),
    force: bool = typer.Option(..., help="Force", prompt="Force your start working day")
):
    user = User(name=name, birthday=birthday, city=city, date=start_date)

    typer.secho("""Create new user""",bg=typer.colors.BRIGHT_BLACK)
    if force:
        fg=typer.colors.GREEN
    else:
        fg=typer.colors.RED

    typer.secho(f"\n{user}",fg=fg)


if __name__ == "__main__":
    typer.run(main)
