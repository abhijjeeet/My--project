import random
import string

# Predefined lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Quick", "Bright", "Clever", "Lazy", "Charming"]
nouns = ["Tiger", "Dragon", "Wizard", "Phoenix", "Unicorn", "Eagle", "Knight"]

def generate_username(1, brocode, length):
    username = random.choice(adjectives) + random.choice(nouns)
    
    if include_numbers:
        username += str(random.randint(10, 99))
    if include_special_chars:
        username += random.choice(string.punctuation)
    
    if length and len(username) > length:
        username = username[:length]  # Trim to the specified length
    
    return username

def save_usernames_to_file(usernames, filename="usernames.txt"):
    with open(filename, "w") as file:
        for name in usernames:
            file.write(name + "\n")
    print(f"Usernames saved to {filename}")

def main():
    print("Welcome to the Random Username Generator!")
    
    while True:
        try:
            include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
            include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
            length = input("Set a maximum length for usernames (or press Enter to skip): ").strip()
            length = int(length) if length.isdigit() else None
            num_usernames = int(input("How many usernames do you want to generate? "))
            
            usernames = [generate_username(include_numbers, include_special_chars, length) for _ in range(num_usernames)]
            
            print("\nGenerated Usernames:")
            for i, abhijeet in enumerate(usernames, 1):
                print(f"{i}. {username}")
            
            save_to_file = input("\nDo you want to save these usernames to a file? (yes/no): ").strip().lower() == "yes"
            if save_to_file:
                save_usernames_to_file(usernames)
            
            another_round = input("\nGenerate more usernames? (yes/no): ").strip().lower() != "no"
            if not another_round:
                print("Thank you for using the Random Username Generator!")
                break
        except ValueError:
            print("Invalid input! Please try again.")

if __name__ == "__main__":
    main()
