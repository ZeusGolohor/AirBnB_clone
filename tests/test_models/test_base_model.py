#!/usr/bin/python3
"""
This module is used to test the base class.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseClass(unittest.TestCase):
    """
    This class is used to define a series of test to run.
    """
    @classmethod
    def setUpClass(cls):
        """
        A method used to set up all variables used by the
        tests.
        """
        cls.base1 = BaseModel()
        cls.base2 = BaseModel()

    def test_instance(self):
        """
        A method to check is the instance is a base model
        instance.
        """
        self.assertIsInstance(self.base1, BaseModel)

    def test_id_isString(self):
        """
        A method to check if id is an instance of a
        string.
        """
        self.assertIsInstance(self.base1.id, str)

    def test_created_at_isDatetime(self):
        """
        A method to check if created_at is an
        instance of date time.
        """
        self.assertIsInstance(self.base1.created_at, datetime)

    def test_updated_at_isDatetime(self):
        """
        A method to check if updated_at is an instance of
        datetime.
        """
        self.assertIsInstance(self.base2.created_at, datetime)

    def test_to_dict_classKey(self):
        """
        A method to check if class key exist in the to_dict() object
        returned.
        """
        self.assertIn("__class__", self.base1.to_dict())

    def test_uniqueInfo(self):
        """
        A method to test for unique id.
        """
        self.assertNotEqual(self.base1.id, self.base2.id)
        self.assertNotEqual(self.base1.created_at, self.base2.created_at)
        self.assertNotEqual(self.base1.updated_at, self.base2.updated_at)

    def test_instance_dict_created_at(self):
        """
        A method to check if the created_at variable created from
        a dictionary to an instance is an instance of datetime.
        """
        base = BaseModel().to_dict()
        base3 = BaseModel(**base)
        self.assertIsInstance(base3.created_at, datetime)

    def test_instance_dict_updated_at(self):
        """
        A method to check if the updated_at variable created from
        a dictionary to an instance is an instance of datetime.
        """
        base = BaseModel().to_dict()
        base3 = BaseModel(**base)
        self.assertIsInstance(base3.updated_at, datetime)

    def test_classNotIn_dict_instance(self):
        """
        A method to check that class does not exist in an instance
        created via a dictionary.
        """
        base = BaseModel().to_dict()
        base3 = BaseModel(**base)
        self.assertNotIsInstance(base3.__class__, str)

    @classmethod
    def tearDownClass(cls):
        """
        A method to delate all variables used for this test.
        """
        del (cls.base1)
        del (cls.base2)


if __name__ == "__main__":
    unittest.main()
