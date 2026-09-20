# Importing string module, provides useful constants for checking character types
# like uppercase letters, digits and special characters

import string

#Check if the given password is in a list of common passwords.

def check_common_password(password):
    with open("common_passwords.txt", "r", encoding="utf-8") as file:
        common = file.read().splitlines()
    if password in common:
        return True
    else:
        return False

# Assess password strength based on length, upper and lowercase letters, special characters, and digits.

def password_strength(password):
    score = 0
    length = len(password)

    upper_case = any(c.isupper() for c in password)
    lower_case = any(c.islower() for c in password)
    special = any(c in string.punctuation for c in password)
    digits = any(c.isdigit() for c in password)

    characters = [upper_case, lower_case, special, digits]

# Assign a corresponding score value.

    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 17:
        score += 1
    if length > 20:
        score += 1

    score += sum(characters) - 1

# Return a string that describes the score.

    if score < 4:
        return "Weak", score
    elif score == 4:
        return "Okay", score
    elif 4 < score <6:
        return "Good", score
    else:
        return "Excellent", score

# Provide useful feedback to the user for improving their password.

def feedback(password):
    if check_common_password(password):
        return "Password was found in a list of commonly used passwords. Score: 0/7"

    strength, score = password_strength(password)

    feedback = f"Acceptable password! Password strength: {strength} (Score: {score}/7)\n"

    if score < 4:
        feedback += "Here are some suggestions to strengthen your password:\n"
        if len(password) <= 8:
            feedback += "- Make sure your password is at least 8 characters in length. \n"
        if not any(c.isupper() for c in password):
            feedback += "- Include at least one uppercase letter. \n"
        if not any(c.islower() for c in password):
            feedback += "- Include at least one lowercase letter. \n"
        if not any(c in string.punctuation for c in password):
            feedback += "- Include at least one special character (e.g., @, #, $).\n"
        if not any(c.isdigit() for c in password):
            feedback += "- Include at least one number.\n"

    return feedback

# Ask the user to input a password and then print the feedback.

password = input("Enter your password: ")
print(feedback(password))