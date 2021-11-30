from dataclasses import fields


class DataclassDTO:
    """ To use this DTO, your dataclass decorator must be set with init=False.
        e.g: @dataclass(init=False)
    """

    def __init__(self, **kwargs):
        dto_fields = (field.name for field in fields(self.__class__))
        for key, value in kwargs.items():
            if key in dto_fields:
                setattr(self, key, value)
