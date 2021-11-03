from PyInquirer import prompt
from database import store_expense, store_new_element
from user import fetch_users


expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },
    {
        "type": "checkbox",
        "name": "userchosen",
        "message": "Which ones owes you money ? 💰",
        'qmark': '✔️',
        "choices": fetch_users()
    }

]

def is_expense_valid(expense):
    expense = list(expense.values())
    if (len(expense) < 3):
        print('Provide valid number of informations 3️⃣')
        return False
    
    if len(expense[0]) <= 0 or len(expense[1]) <= 0 or len(expense[2]) <= 0:
        print('Please provide valid informations ❎')
        return False
    try:
        expense[0] = int(expense[0])
        if (len(expense) == 4):
            expense[3] = list(expense[3])
    except Exception as e:
        return False
    return type(expense[0]) is int and type(expense[1]) is str and type(expense[2]) is str




def new_expense(*args):
    is_test = len(args) > 0
    if not is_test:
        infos = prompt(expense_questions)
    else:
        infos = args
    if not is_expense_valid(infos):
        print('The expense is not valid')
        return False
    is_stored = store_expense(is_test, infos)
    if is_stored:
        print("Expense Added !")
        return True
    print('Could not stored your object')
    return False


