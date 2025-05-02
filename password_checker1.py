import re

def calculate_strength(password):
    score = 0

    # Length points
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Character checks
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    return score

def evaluate_strength(score):
    if score <= 2:
        return "Weak"
    elif 3 <= score <= 4:
        return "Moderate"
    else:
        return "Strong"

def main():
    password = input("Enter your password: ")
    score = calculate_strength(password)
    strength = evaluate_strength(score)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()
