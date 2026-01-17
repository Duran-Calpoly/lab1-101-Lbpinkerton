def check_multiple(number):
    """Check if the number is a multiple of both 3 and 5."""
    return number % 3 == 0 and number % 5 == 0
def check_password(input_string):
    secret_word = "Python123"
    if input_string == secret_word:
        return "access granted"
    else:
        return "access denied"
def calculate_federal_tax(salary):
    """Calculate federal tax based on salary brackets."""
    if salary <= 11000:
        tax_rate = 0.10
    elif salary <= 44725:
        tax_rate = 0.12
    elif salary <= 95375:
        tax_rate = 0.22
    elif salary <= 182100:
        tax_rate = 0.24
    else:
        tax_rate = 0.32
    return salary * tax_rate