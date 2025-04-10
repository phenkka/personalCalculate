from scripts import Scripts


def show_menu() -> None:
    """
    Показать меню для выбора действия
    :return: None
    """
    print(
        "1 - Add expense\n"
        "2 - Show all expenses\n"
        "3 - Show total amount expenses\n"
        "4 - Show expenses by category\n"
        "5 - Clear all expenses\n"
        "6 - Exit\n"
    )


def main():
    """
    Главная функция программы
    :return: None
    """

    """Я чтото только до элифов допер, пример который вы показывали, нуу я не думаю, что здесь он норм"""
    """Там ниже все понятно, думаю комменты излишне"""
    s = Scripts()

    while True:
        show_menu()
        choice = input("Hmm... 🤔 what would you like to do? (1-6)\n")

        if choice == "1":
            try:
                amount = float(input("Enter the amount of the spend 💲: "))
                category = input("Enter a category 📋: ")
                description = input("Enter a description 📃: ")
                s.add_expense(amount, category, description)
                print("So... I've added expenses.")
            except ValueError:
                print("👿 Uh, well, enter the existing amount.")

        elif choice == "2":
            while True:
                expenses = s.get_expenses()
                for key, (amount, category, description) in expenses.items():
                    print(f"{key + 1}: {amount} BTC | {category} | {description}")
                    print("\n\nP.S. 😮 HOW MUCH ARE YOU SPENDING?!")
                back = input("\nEnter 'b' to return to the menu: ").lower()
                if back == 'b':
                    print()
                    break

        elif choice == "3":
            while True:
                print(f"Total spent: {s.get_total()} BTC 💰"
                      "\n\nP.S. 🙄 AND THEN HOW MUCH DO YOU MAKE?")
                back = input("\nEnter 'b' to return to the menu: ").lower()
                if back == 'b':
                    print()
                    break

        elif choice == "4":
            while True:
                category = input("\nEnter a category to filter (or 'b' to return): ")
                if category.lower() == 'b':
                    print()
                    break

                results = s.get_by_category(category)
                if results:
                    for index, (amount, desc) in enumerate(results):
                        print(f"{index + 1} | {amount} 💸 | {desc} "
                              f"\n\nP.S. 😯 WELL, I'M AN AI, BUT I STILL HAVEN'T SEEN ANY ASSETS LIKE THAT.")
                else:
                    print("No expenses found in this category.")

        elif choice == "5":
            while True:
                confirm = input("Are you sure you want to delete all spending? (y/n, or 'b' for return): ").lower()
                if confirm == 'y':
                    s.clear_expenses()
                    print("That's it, all deleted.")
                    break
                elif confirm == 'b' or confirm == 'n':
                    break
                else:
                    print("👿 Uh, well, type in 'y' or 'n' or 'b'.")

        elif choice == "6":
            print("😅 Bye-bye mone... (coughs) ow")
            break

        else:
            print("😢 I can't do that. Enter the number of the operation I know.")


if __name__ == "__main__":
    """
    Точка входа в программу
    :return: None
    """
    print(
        "\nHi Egor 👋, I'm your personal spending assistant ByeByeMoney 💸.\n"
        "I'll help you 🧒 keep track of your spending,\n"
        "you can also find out 🔍 what you spent on and how much you spent in total 💰.\n"
    )
    main()
