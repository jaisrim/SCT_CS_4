from datetime import datetime

def save_log(module_name, details):
    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    with open("activity_log.txt", "a") as file:
        file.write("\n")
        file.write("=" * 50 + "\n")
        file.write(f"Date & Time : {current_time}\n")
        file.write(f"Module      : {module_name}\n")
        file.write(details)
        file.write("\n")

def menu() :
    print("=" * 40)
    print("CYBER ACTIVITY MONITOR")
    print("=" * 40)
    print("1. Text Analyzer")
    print("2. Password Strength Checker")
    print("3. Keyboard Shortcut Guide")
    print("4. View Activity Log")
    print("5. Exit")

def text_analyzer():
    text = input("\nEnter your text: ")

    characters = len(text)
    words = len(text.split())

    uppercase = 0
    lowercase = 0
    digits = 0
    special = 0
    spaces = 0

    for letter in text:
        if letter.isupper():
            uppercase += 1

        elif letter.islower():
            lowercase += 1

        elif letter.isdigit():
            digits += 1

        elif letter.isspace():
            spaces += 1

        else:
            special += 1

    print("\n----- Text Analysis -----")
    print(f"Characters : {characters}")
    print(f"Words      : {words}")
    print(f"Uppercase  : {uppercase}")
    print(f"Lowercase  : {lowercase}")
    print(f"Digits     : {digits}")
    print(f"Spaces     : {spaces}")
    print(f"Special    : {special}")

    details = f"""
Characters : {characters}
Words      : {words}
Uppercase  : {uppercase}
Lowercase  : {lowercase}
Digits     : {digits}
Spaces     : {spaces}
Special    : {special}
"""

    save_log("Text Analyzer", details)

def password_checker():
    password = input("\nEnter your password: ")

    score = 0

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    if len(password) >= 8:
        score += 1

    for letter in password:
        if letter.isupper():
            has_upper = True

        elif letter.islower():
            has_lower = True

        elif letter.isdigit():
            has_digit = True

        elif not letter.isalnum():
            has_special = True

    if has_upper:
        score += 1

    if has_lower:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    print("\n===== Password Analysis =====")
    print("Length (8+)       :", "✓" if len(password) >= 8 else "✗")
    print("Uppercase         :", "✓" if has_upper else "✗")
    print("Lowercase         :", "✓" if has_lower else "✗")
    print("Digit             :", "✓" if has_digit else "✗")
    print("Special Character :", "✓" if has_special else "✗")

    print(f"\nPassword Score : {score}/5")

    if score == 5:
        print("Password Strength : Strong")
    elif score >= 3:
        print("Password Strength : Medium")
    else:
        print("Password Strength : Weak")

    details = f"""
Password Score : {score}/5
"""

    save_log("Password Strength Checker", details)

def keyboard_shortcuts():
    while True:
        print("\n===== Keyboard Shortcut Guide =====")
        print("1. Copy")
        print("2. Paste")
        print("3. Cut")
        print("4. Undo")
        print("5. Redo")
        print("6. Save")
        print("7. Select All")
        print("8. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\nCopy")
            print("Shortcut : Ctrl + C")
            print("Description : Copies the selected text or file.")

        elif choice == "2":
            print("\nPaste")
            print("Shortcut : Ctrl + V")
            print("Description : Pastes the copied content.")

        elif choice == "3":
            print("\nCut")
            print("Shortcut : Ctrl + X")
            print("Description : Cuts the selected text or file.")

        elif choice == "4":
            print("\nUndo")
            print("Shortcut : Ctrl + Z")
            print("Description : Reverses the last action.")

        elif choice == "5":
            print("\nRedo")
            print("Shortcut : Ctrl + Y")
            print("Description : Restores the last undone action.")

        elif choice == "6":
            print("\nSave")
            print("Shortcut : Ctrl + S")
            print("Description : Saves the current file.")

        elif choice == "7":
            print("\nSelect All")
            print("Shortcut : Ctrl + A")
            print("Description : Selects all text or files.")

        elif choice == "8":
            print("\nReturning to Main Menu...")
            break

        else:
            print("Invalid Choice!")

def view_activity_log():
    try:
        with open("activity_log.txt", "r") as file:
            print("\n" + "=" * 50)
            print("         ACTIVITY LOG")
            print("=" * 50)
            print(file.read())
            print("=" * 50)

    except FileNotFoundError:
        print("\nNo activity log found.")

while True:
    menu()
    choice = input("\nEnter your choice: ")

    if choice == "1":
        text_analyzer()

    elif choice == "2":
        password_checker()

    elif choice == "3":
        keyboard_shortcuts()

    elif choice == "4":
        view_activity_log()

    elif choice == "5":
        save_log("Main Menu", "User chose to exit.")
        print("\nThank you for using Cyber Activity Monitor!")
        break

    else:
        print("Invalid choice! Please try again.")

