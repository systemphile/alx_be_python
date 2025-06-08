def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            shopping_list.append(input("Enter a new item: "))
        elif choice == '2':
            # Prompt for and remove an item
            rm = input("Enter an item for deletion: ")
            if rm in shopping_list:
                shopping_list.remove(rm)
            else:
                print(f"{rm} is not in the shopping list")
        elif choice == '3':
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()