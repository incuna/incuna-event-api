from incuna_test_utils.testcases.api_request import APIRequestTestCase as Base

from .factories import UserFactory


class APIRequestTestCase(Base):
    user_factory = UserFactory
