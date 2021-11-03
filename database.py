import csv
import os


def store_new_element(new_element: dict, file_name: str) -> bool:
  '''
  Function to store a new element in database
  Parameters:
    element : An element
  '''

  fieldnames = new_element.keys()
  file_exists = os.path.isfile(file_name) and os.stat(file_name).st_size != 0
  try:
    with open(file_name, 'a+') as file:
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      if not file_exists:
        writer.writeheader()
      writer.writerow(new_element)
    return True
  except Exception as e:
    print(e)
    return False


def store_expense(is_test, infos):
    if is_test:
        dict_test = {'amount': infos[0], 'label': infos[1], 'spender': infos[2]}
        return store_new_element(dict_test, 'test_expense_report.csv')
    else:
        return store_new_element(infos, 'expense_report.csv')