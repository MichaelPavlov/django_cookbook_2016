from decimal import Decimal

from django.contrib.gis.geos import GEOSGeometry
from faker.generator import random
from faker.providers import BaseProvider


class GEODataProvider(BaseProvider):
    poly = (
        (40.34026, 19.15120),
        (42.21670, 26.13934),
        (35.55680, 29.38280),
        (34.15370, 22.58810),
    )

    @classmethod
    def geo_point(cls):
        point_str = 'POINT({} {})'.format(cls.longitude(), cls.latitude())
        return GEOSGeometry(point_str)

    @classmethod
    def latitude(cls):
        l = list(map(lambda t: int(t[0] * 10000000), cls.poly))
        return Decimal(str(random.randint(min(l), max(l)) / 10000000.0)).quantize(Decimal('.000001'))

    @classmethod
    def longitude(cls):
        l = list(map(lambda t: int(t[1] * 10000000), cls.poly))
        return Decimal(str(random.randint(min(l), max(l)) / 10000000.0)).quantize(Decimal('.000001'))
