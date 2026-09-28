# Week 7 - Part B: Shopping List Manager

shopping_list = []

while True:
    print("\nShopping List Manager")
    print("add / remove / show / done")

    choice = input("Enter your choice: ").lower()

    if choice == "add":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(item, "has been added.")

    elif choice == "remove":
        item = input("Enter the item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "has been removed.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if len(shopping_list) == 0:
            print("Your shopping list is empty.")
        else:
            print("Your shopping list:")
            for item in shopping_list:
                print("-", item)

    elif choice == "done":
        print("Goodbye! Thank you for using the Shopping List Manager.")
        break

    else:
        print("Invalid choice. Please choose add, remove, show, or done.")