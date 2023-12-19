import random
import string

common_passwords = [
    "password",
    "123456",
    "qwerty",
    "abc123",
    "letmein",
    # Add more common passwords here
]

common_usernames = [
    "admin",
    "user",
    "guest",
    "test",
    "demo",
    # Add more common usernames here
]

def generate_password_from_list(password_list):
    password = random.choice(password_list).strip()
    password = ''.join(random.choice(password) for _ in range(len(password)))
    return password

def generate_username_from_list(username_list):
    username = random.choice(username_list).strip()
    username = ''.join(random.choice(username) for _ in range(len(username)))
    return username

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

usernames = [
    random.choice([generate_username(username_length), generate_username_from_list(common_usernames)])
    for _ in range(num_users)
]

passwords = [
    random.choice([generate_password(password_length), generate_password_from_list(common_passwords)])
    for _ in range(num_users)
]
# print(usernames)
# print(passwords)

# Print the generated usernames and passwords
for username, password in zip(usernames, passwords):
    pass
    # print(f"Username: {username}, Password: {password}")