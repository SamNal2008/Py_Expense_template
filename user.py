from PyInquirer import prompt
from database import store_new_element
import csv

user_questions = [
    {
        "type": "input",
        "name": "username",
        "message": "What is your new user name ?"
    },
    {
        "type": "confirm",
        "name": "confirmed",
        "message": "Are you sure you want to add this user ?"
    }
]

def add_user():
    user_infos = prompt(user_questions)
    print(user_infos)
    if (user_infos['confirmed']):
        store_new_element(user_infos, 'user_report.csv')
    return True

def fetch_users():
    res = []
    with open('user_report.csv', 'r') as f:
        reader = csv.DictReader(f, fieldnames=['username', 'confirmed'])
        for user in reader:
            if user['username'] == 'username':
                continue
            is_user_valid = bool(user['confirmed'])
            if is_user_valid:
                res.append({'name': user['username']})
    return res