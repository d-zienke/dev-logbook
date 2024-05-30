from database import add_entry, get_entries, create_table, drop_table


def prompt_entry():
  entry_body = input("Wprowadź treść: ")
  entry_date = input("Wprowadź datę: ")
  add_entry(entry_body, entry_date)


def view_entries(entries):
  for entry in entries:
    print(f"{entry[1]}:\n{entry[0]}\n")
    # this will work if we use `connection.row_factory = sqlite3.Row`
    # print(f"{entry['entry_date']}:\n{entry['entry_body']}")


welcome_msg = "Witaj w Dzienniku Developera!"

menu = """
Wybierz jedną z poniższych akcji:
1 - dodaj wpis
2 - przejrzyj wpisy
3 - wyjdź z programu
"""

menu_action_prompt = "Twój wybór: "

# drop_table()
create_table()
print(welcome_msg)
print(menu)

while (user_action:=input(menu_action_prompt))!="3":
  match(user_action):
    case "1":
      print("dodawanie wpisu...")
      prompt_entry()
    case "2":
      print("przeglądanie wpisów...")
      view_entries(get_entries())
    case _:
      print("nieznana akcja")
  print(menu)
  
print("koniec programu...")