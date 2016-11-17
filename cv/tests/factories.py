import factory
from factory import lazy_attribute
from faker import Factory
# from django.utils.module_loading
from cv.models import CV

faker = Factory.create('ru_RU')


class CVFactory(factory.DjangoModelFactory):
    class Meta:
        model = CV

    first_name = lazy_attribute(lambda o: faker.first_name())
    last_name = lazy_attribute(lambda o: faker.last_name())
    email = lazy_attribute(lambda o: faker.email())



def fill_db():
    cvs = CVFactory.create_batch(3)