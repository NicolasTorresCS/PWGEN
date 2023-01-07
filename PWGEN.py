import random
import string

def generate_password(length):
    # Generate a random password using lowercase, uppercase, and digits
    password_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password

def main():
    # Generate a random password with 15 characters
    password = generate_password(15)
    
    # Save the password to a text file
    with open('password.txt', 'w') as f:
        f.write(password)
    print(f'Password saved to password.txt: {password}')

if __name__ == '__main__':
    main()