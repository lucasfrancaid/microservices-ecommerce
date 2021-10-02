from service.core.entities.repository import RepositoryConfigurationEntity


def test_repository_configuration_entity_none():
    configuration_entity = RepositoryConfigurationEntity()

    assert configuration_entity.host is None
    assert configuration_entity.port is None
    assert configuration_entity.name is None
    assert configuration_entity.username is None
    assert configuration_entity.password is None
    assert configuration_entity.use_ssl is False
    assert configuration_entity.ssl_certfile is None
