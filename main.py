from PyInquirer import prompt
from examples import custom_style_2
from expense import expense_questions,new_expense
from user import add_user
import subprocess

def ask_option():
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v0.1",
        "choices": ["New Expense 💸","Show Status 📜","New User 🤦", "Launch tests 🧪", "Exit"]
    }
    option = prompt(main_option)
    if (option['main_options']) == "New Expense 💸":
        new_expense()
        ask_option()
    elif option['main_options'] == "New User 🤦":
        add_user()
        ask_option()
    elif (option['main_options']) == "Exit":
        print('Good bye ! 👋')
    elif option['main_options'] == 'Launch tests 🧪':
        subprocess.run(['python3', '-m unittest discover ./tests/'])
    else:
        print('Sorry this feature is not implemented yet 😢')

def main():
    ask_option()

main()