from datetime import date
import emoji

from application.salary import calculate_salary
from application.db.people import get_employees


def get_today():
    print(date.today())


if __name__ == '__main__':
    get_today()
    calculate_salary()
    get_employees()
    print(emoji.emojize('Python is :thumbs_up:'))
