from src.application.patterns.singleton import Singleton


def test_singleton():

    class Generic(metaclass=Singleton):
        ...

    instance_1 = Generic()
    instance_2 = Generic()

    assert instance_1 == instance_2
