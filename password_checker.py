import re

def check_password_strength(password):
    strength = "Weak"

    if len(password) >= 8:
        if re.search("[a-z]", password) and re.search("[A-Z]", password):
            if re.search("[0-9]", password):
                if re.search("[@#$%^&*!]", password):
                    strength = "Strong"
                else:
                    strength = "Medium"
            else:
                strength = "Medium"
    return strength


password = input("Enter password: ")
result = check_password_strength(password)

print("Password Strength:", result)