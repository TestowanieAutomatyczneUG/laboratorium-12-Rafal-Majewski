from modules.Subscriber import Subscriber
from modules.Client import Client
from unittest.mock import patch, call
import unittest

class Test_Subscriber(unittest.TestCase):
	def setUp(self):
		self.subscriber = Subscriber()

	def test_addClient_if_adds(self):
		client = Client()
		with patch.object(self.subscriber, "clients") as mock_clients:
			self.subscriber.addClient(client)
			mock_clients.add.assert_called_once_with(client)

	def test_addClient_if_raises_type_error(self):
		with self.assertRaises(TypeError):
			self.subscriber.addClient("client")

	def test_removeClient_if_removes(self):
		client = Client()
		with patch.object(self.subscriber, "clients") as mock_clients:
			self.subscriber.removeClient(client)
			mock_clients.remove.assert_called_once_with(client)

	def test_removeClient_if_raises_type_error(self):
		with self.assertRaises(TypeError):
			self.subscriber.removeClient("client")

	def test_notifyAllClients(self):
		client1 = Client()
		with patch.object(client1, "notify") as mock_notify:
			with patch.object(self.subscriber, "clients", [client1]):
				self.subscriber.notifyAllClients("test hello")
				mock_notify.assert_called_once_with("test hello")

	def test_notifyAllClients_many_clients(self):
		with patch.object(Client, "notify") as mock_notify:
			with patch.object(self.subscriber, "clients", [Client(), Client()]):
				self.subscriber.notifyAllClients("test hello")
				mock_notify.assert_has_calls([call("test hello"), call("test hello")])

	def test_notifyAllClients_if_raises_type_error(self):
		with self.assertRaises(TypeError):
			self.subscriber.notifyAllClients(1)

	def test_notifyClient(self):
		client = Client()
		with patch.object(client, "notify") as mock_notify:
			with patch.object(self.subscriber, "clients", [client]):
				self.subscriber.notifyClient(client, "test hello")
				mock_notify.assert_called_once_with("test hello")

	def test_notifyClient_if_raises_value_error_for_not_in_clients(self):
		with patch.object(self.subscriber, "clients", []):
			with self.assertRaises(ValueError):
				self.subscriber.notifyClient(Client(), "test hello")