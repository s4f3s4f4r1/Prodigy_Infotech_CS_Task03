
# PassFortify

PassFortify is a simple Python-based Password Strength Checker that evaluates the strength of a user-provided password and provides suggestions for improvement if necessary.
### s4f3s4f4r1 
Developer of this password checking tool.
## Overview

PassFortify checks the strength of a password based on several criteria, including the presence of uppercase letters, digits, and special characters. It will inform the user whether their password is weak, moderate, or strong and suggest improvements for weak passwords.

## Features

- **Password Strength Evaluation**: Checks if the password is weak, moderate, or strong.
- **Improvement Suggestions**: Provides actionable suggestions to make a weak password stronger.
- **Interactive Tool**: Prompts the user to input a password and provides immediate feedback.

## How to Use

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd Task03_pass_Fortify
    ```

3. Run the PassFortify script with `python3`:

    ```bash
    python3 Task_03_PassFortify.py
    ```

4. You will be prompted to enter a password for strength evaluation:

    ```plaintext
    Enter your password to check its strength: password
    ```

5. Based on the password, PassFortify will provide a strength rating (Weak, Moderate, or Strong) and offer suggestions for improvement if the password is weak.

## Sample Output

### Weak Password Example

```plaintext
Enter your password to check its strength: password
Password strength: Weak

Suggestions to improve your password:
- Password should contain at least one uppercase letter.
- Password should contain at least two or more digits.
- Password should contain at least two or more special characters.
