from dataclasses import dataclass

from src.application.patterns.dto import DataclassDTO


def test_dto_pattern_for_dataclasses():

    @dataclass(init=False)
    class GenericEntity(DataclassDTO):
        name: str
        age: int

    generic_dict = {'name': 'Lucas', 'age': 20, 'phone': '+55'}

    entity = GenericEntity(**generic_dict)

    assert entity.name == generic_dict['name']
    assert entity.age == generic_dict['age']
    assert not getattr(entity, 'phone', None)
