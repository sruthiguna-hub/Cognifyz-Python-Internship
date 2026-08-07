# Email Validator
def validate_email(email):
    if "@" in email and "." in email:
        at_position = email.index("@")
        dot_position = email.rindex(".")

        if at_position > 0 and dot_position > at_position + 1 and dot_position < len(email) - 1:
            return True
    return False
email = input("Enter your email address: ")
if validate_email(email):
    print("Valid Email Address")
else:
    print("Invalid Email Address")