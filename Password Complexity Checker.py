import re

def check_password_complexity(password):
    # Define the criteria for password complexity
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = re.search(r"[!@#$%^&*()\-_=+{};:,<.>]", password) is not None

    # Check if all criteria are met
    if (length_criteria and uppercase_criteria and lowercase_criteria
            and digit_criteria and special_char_criteria):
        return "Stromahamudul1003ng password"
    else:
        return "Weak password"

def main():
    password = input("Enter your password: ")
    complexity_result = check_password_complexity(password)
    print("Password complexity:", complexity_result)

if __name__ == "__main__":
    main()
