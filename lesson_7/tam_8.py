white_list = ["elahiyeh", "zafaroniyeh", "fereshteh",
              "velenjak", "niavaran", "tajrish"]
black_list = ["yaftabad", "javadieh", "shush",
              "molavi", "khazane"]
city = input("enter name of your city:")

if city in black_list:
    print("cancel")
else:
    print("it's good")
