import re
import random
import string
from tqdm import tqdm  # To show a status bar

# Function to calculate overall password strength based on length and criteria
def check_password_strength(password):
    if len(password) < 8:
        return "Weak", 20, "\033[91m"  # Red
    elif len(password) < 12:
        return "Medium", 40, "\033[93m"  # Orange (Yellow)
    elif len(password) < 16:
        return "Strong", 60, "\033[92m"  # Green
    else:
        return "Very Strong", 100, "\033[92m"  # Green (Very Strong)

# Function to check if the password meets all required criteria (uppercase, lowercase, number, special character)
def check_criteria(password):
    if not re.search(r"[a-z]", password):  # Lowercase
        return "Invalid", "Missing lowercase letter"
    if not re.search(r"[A-Z]", password):  # Uppercase
        return "Invalid", "Missing uppercase letter"
    if not re.search(r"[0-9]", password):  # Number
        return "Invalid", "Missing number"
    if not re.search(r"[@$!%*?&]", password):  # Special character
        return "Invalid", "Missing special character"
    return "Valid", []

# Function to check for repeated characters or sequences
def check_repeating_or_sequence(password):
    # Check for repeating characters (e.g., aa, 111, !!)
    if re.search(r"(.)\1", password):  # Two consecutive repeating characters
        return True, "Repeating characters detected."
    
    # Check for sequences (e.g., abc, 123, aaa)
    if re.search(r"(012|123|234|345|456|567|678|789|890|abc|def|ghi|jkl|mno|pqr|stu|vwx|yz|zyx)", password):
        return True, "Sequential characters detected."
    
    return False, ""

# Function to generate a very strong password with no sequences or repetitions
def generate_very_strong_password(min_length=16):
    while True:
        # Generate a candidate password
        password = ''.join(random.choices(string.ascii_letters + string.digits + "@$!%*?&", k=min_length))
        
        # Ensure it meets all criteria and has no sequences or repetitions
        if (re.search(r"[a-z]", password) and 
            re.search(r"[A-Z]", password) and 
            re.search(r"[0-9]", password) and 
            re.search(r"[@$!%*?&]", password) and 
            not check_repeating_or_sequence(password)[0]):
            return password

# Function to display password strength with status bar and feedback
def display_status(password):
    # Check if the password is valid first
    validity, missing_criteria = check_criteria(password)

    if validity == "Invalid":
        print(f"Password is \033[91mInvalid\033[0m! ({missing_criteria})")
        
        # Suggest a very strong password for the user
        suggested_password = generate_very_strong_password()
        print(f"Suggested password: {suggested_password}")
        return "Invalid"
    
    # Check for repeating characters or sequences
    has_issue, issue_message = check_repeating_or_sequence(password)

    if has_issue:
        print(f"\033[93mNote: {issue_message}\033[0m")
        strength, progress, color = "Weak", 20, "\033[91m"  # Red
    else:
        # If password is valid, check its strength
        strength, progress, color = check_password_strength(password)

    # Display progress bar with colored strength description
    with tqdm(total=100, desc="Password Strength", ncols=100, bar_format=f"{color}{{l_bar}}{{bar}}| {{n_fmt}}/{{total_fmt}}\033[0m") as pbar:
        pbar.set_postfix_str(f"{color}{strength}\033[0m")
        pbar.update(progress)

    # Display password strength
    print(f"{color}Password Strength: {strength}\033[0m")
    
    # Suggest a very strong password only if necessary (after checking strength and issues)
    if strength == "Weak" or strength == "Medium" or has_issue:
        suggestion = generate_very_strong_password()
        print(f"Suggested password: {suggestion}")
    
    return strength

if __name__ == "__main__":
    password = input("Enter password to check: ")
    display_status(password)
