from locations.tests.factories import LocationFactory


def fake():
    """
    Generates fake test data into database
    :return: None
    """
    locationas = LocationFactory.create_batch(3)
