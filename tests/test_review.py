import unittest
from app.models import Review

class ReviewTest(unittest.TestCase):
  """test behaviour of review class"""
  def setUp(self):
    self.new_review = Review(1200, 'God must be crazy', "htttps://kjhg", "great")

  def test_instance(self):
    self.assertTrue(isinstance(self.new_review, Review))