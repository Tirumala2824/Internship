import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def calculate_password_strength(password):
    length = len(password)
    uppercase_letters = sum(1 for char in password if char.isupper())
    lowercase_letters = sum(1 for char in password if char.islower())
    digits = sum(1 for char in password if char.isdigit())
    special_characters = sum(1 for char in password if char in string.punctuation)

    total_characters = uppercase_letters + lowercase_letters + digits + special_characters
    strength_percentage = total_characters / length
    normalized_strength = (strength_percentage - 0.01) / 1
    return normalized_strength


def main():
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    strength = calculate_password_strength(password)

    print(f"Generated Password: {password}")
    print(f"Strength: {strength:.4f}")  # Strength normalized between 0 and 1, excluding 0 and 1


if __name__ == "__main__":
    main()
