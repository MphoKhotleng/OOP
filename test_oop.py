import pytest
from oop import Person

def test_hello():
    person = Person('Singi',24, 'male', 'being helpful, smiling and skating.')
    assert person.hello() == 'Hello, my name is Singi and I am 24 years old. My interests are being helpful, smiling and skating.'