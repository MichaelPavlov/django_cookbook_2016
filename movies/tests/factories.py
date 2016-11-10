import factory
from factory import lazy_attribute
from faker import Factory

from movies.models import Genre, Director, Actor, Movie

faker = Factory.create('ru_RU')


class GenreFactory(factory.DjangoModelFactory):
    class Meta:
        model = Genre

    title = lazy_attribute(lambda o: faker.company())


class DirectorFactory(factory.DjangoModelFactory):
    class Meta:
        model = Director

    first_name = lazy_attribute(lambda o: faker.first_name())
    last_name = lazy_attribute(lambda o: faker.last_name())


class ActorFactory(factory.DjangoModelFactory):
    class Meta:
        model = Actor

    first_name = lazy_attribute(lambda o: faker.first_name())
    last_name = lazy_attribute(lambda o: faker.last_name())


class MovieFactory(factory.DjangoModelFactory):
    class Meta:
        model = Movie

    title = lazy_attribute(lambda o: faker.name())
    rating = lazy_attribute(lambda o: faker.pyint())

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for genre in extracted:
                self.genres.add(genre)

    @factory.post_generation
    def directors(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for director in extracted:
                self.directors.add(director)

    @factory.post_generation
    def actors(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for actor in extracted:
                self.actors.add(actor)


def fill_db():
    genres = GenreFactory.create_batch(3)
    directors = DirectorFactory.create_batch(3)
    actors = ActorFactory.create_batch(3)
    MovieFactory.create_batch(3, genres=genres, actors=actors, directors=directors)
