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

    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    while PainInformation.objects.filter(code=code).exists():
        code = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))
    return code
