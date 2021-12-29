import unittest
import requests

class Test_randomuser(unittest.TestCase):
	def setUp(self):
		self.responseData = requests.get("https://randomuser.me/api/").json()

	def test_if_info_field_is_in_response(self):
		self.assertIn("info", self.responseData)

	def test_if_results_field_is_in_response(self):
		self.assertIn("results", self.responseData)

	def test_if_results_field_is_list(self):
		self.assertIsInstance(self.responseData["results"], list)

	def test_if_length_in_info_matches_results_length(self):
		self.assertEqual(self.responseData["info"]["results"], len(self.responseData["results"]))

	def test_if_email_has_correct_format(self):
		for user in self.responseData["results"]:
			self.assertRegex(user["email"], r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

	def test_if_gender_valid(self):
		for user in self.responseData["results"]:
			self.assertIn(user["gender"], ["male", "female"])

	def test_if_coordinates_is_dict(self):
		for user in self.responseData["results"]:
			self.assertIsInstance(user["location"]["coordinates"], dict)
