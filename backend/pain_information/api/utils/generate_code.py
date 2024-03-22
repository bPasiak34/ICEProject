import random
import string
from api.models import PainInformation

def generate_code(length: int) -> str:
    """Function used to generate a random code for the PainInformation model."""
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    while PainInformation.objects.filter(code=code).exists():
        code = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))
    return code


class GenerateCode:
    def __init__(self, length: int):
        self.length = length
        
    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value < 1:
            raise ValueError("Length must be greater than or equal to 1.")
        self._length = value
            
    def __call__(self):
        return generate_code(self.length)