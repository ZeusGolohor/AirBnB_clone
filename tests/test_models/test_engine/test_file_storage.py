#!/usr/bin/python
"""
This module is used to test the file storage.
"""
import unittest
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    This class is used to test the file storage.
    """
    @classmethod
    def setUpClass(cls):
        """
        A method used to set up this class for testing.
        """
        cls.base1 = BaseModel()
        cls.base1.save()

    def test_storage_works(self):
        """
        To check if the storage is not empty.
        """
        self.assertIsNotNone(storage.all())

    def test_new_save_reloaded_instance(self):
        """
        To check if a new instance exist in the file system
        objects.
        """
        self.assertIn("{}.{}".format(
                            self.base1.__class__.__name__,
                            self.base1.id),
                    storage._FileStorage__objects
                    )

    @classmethod
    def tearDownClass(cls):
        """
        A method used to delete instances that were created during
        test.
        """
        del (cls.base1)
