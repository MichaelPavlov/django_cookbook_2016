from cv.tests.factories import *


def fake():
    """
    Generates fake test data into database
    :return: None
    """
    cvs = CVFactory.create_batch(3)
