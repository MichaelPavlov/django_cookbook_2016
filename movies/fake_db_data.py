from movies.tests.factories import *


def fake():
    """
    Generates fake test data into database
    :return: None
    """
    genres = GenreFactory.create_batch(3)
    directors = DirectorFactory.create_batch(3)
    actors = ActorFactory.create_batch(3)
    MovieFactory.create_batch(300, genres=genres, actors=actors, directors=directors)
