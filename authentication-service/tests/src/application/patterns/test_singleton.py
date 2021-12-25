from src.application.patterns.singleton import Singleton


def test_singleton_pattern():

    class Generic(metaclass=Singleton):
        ...

    instance_1 = Generic()
    instance_2 = Generic()

    assert instance_1 == instance_2
    assert id(instance_1) == id(instance_2)
    assert hash(instance_1) == hash(instance_2)
