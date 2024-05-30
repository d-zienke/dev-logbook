welcome_msg = "Witaj w Dzienniku Developera!"

menu = """
Wybierz jedną z poniższych akcji:
1 - dodaj wpis
2 - przejrzyj wpisy
3 - wyjdź z programu
"""

menu_action_prompt = "Twój wybór: "

print(welcome_msg)
print(menu)

while (user_action:=input(menu_action_prompt))!="3":
  match(user_action):
    case "1":
      print("dodawanie wpisu...")
    case "2":
      print("przeglądanie wpisów...")
    case _:
      print("nieznana akcja")
  print(menu)
  
print("koniec programu...")