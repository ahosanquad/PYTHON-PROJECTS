email = input("Enter your email: ")

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(f"Your Username is {username} and Domain is {domain}")