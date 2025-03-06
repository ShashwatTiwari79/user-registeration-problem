import re
import logging
logging.basicConfig(
    filename='app.log',  # Log file name
    filemode='a',        # Append mode
    level=logging.INFO,  # Logging level
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
def compare_name(name):
    if re.match(r'^[A-Z][a-zA-Z]{2,}$', name):
        logger.info(f'Valid name: {name}')
        return True
    else:
        logger.warning(f'Invalid name: {name}')
        return False
def email_verification(email):
    pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@bl\.co(\.in)?$'
    if re.match(pattern, email):
        logger.info(f'Valid email: {email}')
        return True
    else:
        logger.warning(f'Invalid email: {email}')
        return False
def is_valid_mobile(number):
    pattern = r'^91\s\d{10}$'
    if re.match(pattern, number):
        logger.info(f'Valid mobile number: {number}')
        return True
    else:
        logger.warning(f'Invalid mobile number: {number}')
        return False
def validate_password(password):
    special_chars = re.findall(r"[^a-zA-Z0-9]", password)
    if len(special_chars) != 1:
        logger.warning(f'Invalid password (special characters issue): {password}')
        return False
    if len(password) < 8:
        logger.warning(f'Invalid password (length issue): {password}')
        return False
    if not re.search(r'[A-Z]', password):
        logger.warning(f'Invalid password (uppercase letter missing): {password}')
        return False
    if not re.search(r'\d', password):
        logger.warning(f'Invalid password (digit missing): {password}')
        return False   
    logger.info(f'Valid password: {password}') 
    return True
if __name__ == '__main__':
    first_name = input("Enter your first name:")
    last_name = input("Enter your last name:")
    check_first_name = compare_name(first_name)
    check_second_name = compare_name(last_name)
   
    email = input("Enter your email id:")
    check_email = email_verification(email)
    
    mobile_number = input("Enter your mobile number:")
    check_mobile_number = is_valid_mobile(mobile_number)
    
    password = input("Enter your password:")
    check_password = validate_password(password)
    if check_first_name:
        print("\nfirst name is valid")
    else:
        print("first name is invalid")
    if check_second_name:
        print("last name is valid")
    else:
        print("last name is invalid")
    if check_email:
        print("email is valid")
    else:
        print("email is invalid")
    if check_mobile_number:
        print("mobile number is valid")
    else:
        print("mobile number is invalid")
    if check_password:
        print("password is valid")
    else:
        print("password is invalid")
        