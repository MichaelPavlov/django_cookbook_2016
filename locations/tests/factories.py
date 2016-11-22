import factory
from factory import lazy_attribute
from faker import Factory

from locations.models import Location
from movies.tests.faker_providers import GEODataProvider

faker = Factory.create('ru_RU')
faker.add_provider(GEODataProvider)


class LocationFactory(factory.DjangoModelFactory):
    class Meta:
        model = Location

    title = lazy_attribute(lambda o: faker.name())
    slug = factory.Sequence(lambda n: 'cat-location-slug-{}'.format(n))
    small_image = factory.django.ImageField()
    medium_image = factory.django.ImageField()
    large_image = factory.django.ImageField()
    point = factory.LazyAttribute(lambda x: faker.geo_point())
    # point = models.PointField()
