## Summary:
# Password Complexity Checker Function (check_password_complexity()):

This function takes a password as input and evaluates its complexity based on several criteria:
Length: The password must be at least 8 characters long.
# Uppercase Letters: The password must contain at least one uppercase letter.
# Lowercase Letters: The password must contain at least one lowercase letter.
# Digits: The password must contain at least one digit.
## Special Characters: The password must contain at least one special character from the provided set (!@#$%^&*()\-_=+{};:,<.>).
It returns "Strong password" if all criteria are met; otherwise, it returns "Weak password".
## Main Function (main()):

This function serves as the entry point of the program.
It prompts the user to enter a password.
It calls the check_password_complexity() function with the user-input password and prints the result.


## Implementation Example:
You can run this code by copying it into a Python file (e.g., password_checker.py) and executing it using a Python interpreter. After running the program, you can input different passwords to see how the Password Complexity Checker evaluates their strength. Adjustments to the criteria can be made as per your specific requirements for password strength.
