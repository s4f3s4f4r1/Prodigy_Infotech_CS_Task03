print(" ____               _____          _   _  __        ")
print("|  _ \ __ _ ___ ___|  ___|__  _ __| |_(_)/ _|_   _  ")
print("| |_) / _` / __/ __| |_ / _ \| '__| __| | |_| | | | ")
print("|  __/ (_| \__ \__ \  _| (_) | |  | |_| |  _| |_| | ")
print("|_|   \__,_|___/___/_|  \___/|_|   \__|_|_|  \__, | ")
print("                                             |___/  ")
print("                                                    ")
print("     By s4f3s4f4r1                                  ")

import re

# Function to check the strength of the password
def check_password_strength(password):
    # Initialize feedback and strength score
    feedback = []
    strength = 0

    # Check for password length (minimum 8 characters)
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for presence of uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for presence of lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for presence of digits
    if re.search(r'[0-9]', password):
        strength += 2
    else:
        feedback.append("Password should contain at least two or more digits.")

    # Check for presence of special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 2
    else:
        feedback.append("Password should contain at least two or more special characters.")

    # Strength feedback
    if strength == 7:
        return "Password strength: Strong", feedback
    elif strength >= 4:
        return "Password strength: Medium", feedback
    else:
        return "Password strength: Weak", feedback

# Main function to get user input and provide feedback
def main():
    print("Welcome to the Password Strength Checker!")
    password = input("Enter your password to check its strength: ")

    strength, feedback = check_password_strength(password)

    # Display the password strength
    print("\n" + strength)
    
    # If there are any feedback messages, display them
    if feedback:
        print("\nSuggestions to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")

# Run the tool
if __name__ == "__main__":
    main()
