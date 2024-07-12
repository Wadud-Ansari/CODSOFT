import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Password Generator")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: ").strip())
            if length < 1:
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        
        password = generate_password(length)
        print(f"Generated password: {password}")
        
        another = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Exiting the password generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
