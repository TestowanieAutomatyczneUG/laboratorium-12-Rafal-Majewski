import unittest
import requests
from unittest.mock import patch

class Wrapper:
	def __init__(self, obj):
		self.obj = obj

	def json(self):
		return self.obj


class Test_randomuser(unittest.TestCase):
	@patch("requests.get", return_value=Wrapper({"info": {}}))
	def test_if_info_field_is_in_response(self, mockRequestsGet):
		responseData = requests.get("https://randomuser.me/api/").json()
		self.assertIn("info", responseData)

	@patch("requests.get", return_value=Wrapper({"results": []}))
	def test_if_results_field_is_in_response(self, mockRequestsGet):
		responseData = requests.get("https://randomuser.me/api/").json()
		self.assertIn("results", responseData)

	@patch("requests.get", return_value=Wrapper({"results": []}))
	def test_if_results_field_is_list(self, mockRequestsGet):
		responseData = requests.get("https://randomuser.me/api/").json()
		self.assertIsInstance(responseData["results"], list)

	@patch("requests.get", return_value=Wrapper({"results": [{}, {}], "info": {"results": 2}}))
	def test_if_length_in_info_matches_results_length(self, mockRequestsGet):
		responseData = requests.get("https://randomuser.me/api/").json()
		self.assertEqual(responseData["info"]["results"], len(responseData["results"]))

	@patch("requests.get", return_value=Wrapper({"results": [{"email": "goodheropl@gmail.com"}]}))
	def test_if_email_has_correct_format(self, mockRequestsGet):
		responseData = requests.get("https://randomuser.me/api/").json()
		for user in responseData["results"]:
			self.assertRegex(user["email"], r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

	@patch("requests.get", return_value=Wrapper({"results": [{"gender": "male"}, {"gender": "female"}]}))
	def test_if_gender_valid(self, mockRequestsGet):
		responseData = requests.get("https://randomuser.me/api/").json()
		for user in responseData["results"]:
			self.assertIn(user["gender"], ["male", "female"])

	@patch("requests.get", return_value=Wrapper({"results": [{"location": {"coordinates": {}}}]}))
	def test_if_coordinates_is_dict(self, mockRequestsGet):
		responseData = requests.get("https://randomuser.me/api/").json()
		for user in responseData["results"]:
			self.assertIsInstance(user["location"]["coordinates"], dict)

	@patch("requests.get", return_value=Wrapper({"results": [{"name": {"first": "Maciej"}}]}))
	def test_if_coordinates_is_dict(self, mockRequestsGet):
		responseData = requests.get("https://randomuser.me/api/").json()
		for user in responseData["results"]:
			self.assertIsInstance(user["name"]["first"], str)