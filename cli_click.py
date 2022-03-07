
from datetime import datetime
import click


class User:
    __slots__ = ["name", "birthday", "place", "date"]

    def __init__(self, **args):
        self.name = args.get("name", "")
        self.birthday = args.get("birthday", "")
        self.place = args.get("place", "")
        self.date = args.get("date", "")
        pass

    def __str__(self):
        return f"Hello {self.name} from {self.place}.\nYou birthday is: {self.birthday}.\nYou start wotking at: {self.date}"


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


@click.command()
@click.option("-n", "--name", type=str, required=True, help="Your name", prompt="Eneter Name")
@click.option("-b", "--birthday", type=str, required=True, callback=validate_date, help="Your birthday in DD.MM.YYYY format", prompt="Your birthday in DD.MM.YYYY format")
@click.option("-p", "--place", type=click.Choice(["TelAviv", "Reeshon", "BatYam"], case_sensitive=False), required=True, help="Your city name", prompt="Eneter City", default="BatYam")
@click.option("-d", "--date", type=str, required=True, callback=validate_date, help="The start date", prompt="Eneter start date in DD.MM.YYYY format")
def click_main(name, birthday, place, date):
    user = User(name=name, birthday=birthday, place=place, date=date)
    click.echo(user)

if __name__ == '__main__':
    click_main()
