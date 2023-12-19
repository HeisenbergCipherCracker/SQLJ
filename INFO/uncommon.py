import random
import string

def generate_username(length):
    username = ''.join(random.choices(string.ascii_lowercase, k=length))
    return username

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(alphabet, k=length))
    return password

# Generate a list of usernames and passwords
num_users = 1000
username_length = 8
password_length = 12

usernames = [generate_username(username_length) for _ in range(num_users)]
passwords = [generate_password(password_length) for _ in range(num_users)]

# Print the generated usernames and passwords
for username, password in zip(usernames, passwords):
    print(f"Username: {username}, Password: {password}")