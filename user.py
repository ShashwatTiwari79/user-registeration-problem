import re
def first_name(name):
    if re.match(r'^[A-Z][a-zA-Z]{2,}$', name):
        return True
    else:
        return False
if __name__ == '__main__':
    user_name = input("Enter your first name:")
    check_name = first_name(user_name)
    if check_name:
        print("first name is valid")
    else:
        print("first name is invalid")

