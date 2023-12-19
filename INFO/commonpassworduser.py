import random

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

# Generate a list of passwords and usernames
num_credentials = 20

passwords = [generate_password_from_list(common_passwords) for _ in range(num_credentials)]
usernames = [generate_username_from_list(common_usernames) for _ in range(num_credentials)]

# Print the generated passwords and usernames
for password, username in zip(passwords, usernames):
    print(f"Username: {username}, Password: {password}")