import re
def compare_name(name):
    if re.match(r'^[A-Z][a-zA-Z]{2,}$', name):
        return True
    else:
        return False
def email_verification(email):
    pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@bl\.co(\.in)?$'
    if re.match(pattern, email):
        return True
    else:
        return False
if __name__ == '__main__':
    first_name = input("Enter your first name:")
    last_name = input("Enter your last name:")
    check_first_name = compare_name(first_name)
    check_second_name = compare_name(last_name)
    if check_first_name:
        print("first name is valid")
    else:
        print("first name is invalid")
    if check_second_name:
        print("last name is valid")
    else:
        print("last name is invalid")
    email = input("Enter your email id:")
    check_email = email_verification(email)
    if check_email:
        print("email is valid")
    else:
        print("email is invalid")