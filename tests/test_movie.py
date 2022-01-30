import unittest
from app.models import Movie

class MovieTest(unittest.TestCase):
  """Test class to test the behaviour of the movie class"""

  def setUp(self):
    """set up method that will run before every test"""

    self.new_movie = Movie(1234,'Python Must be crazy', 'A thrilling new Python series','/khsjha27hbs',8.5,129993)

  def test_instance(self):
    self.assertTrue(isinstance(self.new_movie, Movie))