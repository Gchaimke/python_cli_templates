
from datetime import datetime

import click
import typer


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


def main(
    name: str = typer.Option("Chaim","--name","-n", help="Your Name",
                             prompt="Enter your name"),
    birthday: str = typer.Option(
        "10.12.1985", help="Your birthday in YYYY-MM-DD format", callback=validate_date, prompt="Enter your birthday in YYYY-MM-DD format"),
    city: str = typer.Option("TelAviv", help="Your City",
                             prompt="Enter your city"),
    start_date: str = typer.Option(
        "04.04.2022", help="The sart date", callback=validate_date, prompt="Enter your start working day")
):
    """Create new user"""
    user = User(name=name, birthday=birthday, city=city, date=start_date)

    typer.secho(f"\n{user}", fg=typer.colors.GREEN)


if __name__ == "__main__":
    typer.run(main)
