import random
import string

def generate_code(length: int = 6) -> str:
    """
    Function used to generate a random code for the PainInformation model.

    Args:
        length (int): The length of the generated code. Default is 6.

    Returns:
        str: A randomly generated code.
    """
    from api.models import PainInformation  
    
    strings = string.ascii_uppercase.replace('I', '',).replace('O', '') + string.digits + string.ascii_lowercase.replace('l', '')

    code = ''.join(random.choices(strings, k=length))
    while PainInformation.objects.filter(code=code).exists():
        code = ''.join(random.choices(strings, k=length))
    return code
