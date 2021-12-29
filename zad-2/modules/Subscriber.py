from modules.Client import Client

class Subscriber:
	def __init__(self) -> None:
		self.clients = None
	def addClient(self, client: Client) -> None:
		if not isinstance(client, Client):
			raise TypeError("client must be an instance of Client")
		self.clients.add(client)
	def removeClient(self, client: Client) -> None:
		if not isinstance(client, Client):
			raise TypeError("client must be an instance of Client")
		self.clients.remove(client)
	def notifyAllClients(self, message: str) -> None:
		if not isinstance(message, str):
			raise TypeError("message must be an instance of str")
		for client in self.clients:
			self._notifyClient(client, message)
	def _notifyClient(self, client: Client, message: str) -> None:
		client.notify(message)
	def notifyClient(self, client: Client, message: str) -> None:
		if not client in self.clients:
			raise ValueError("client must be in clients")
		if not isinstance(client, Client):
			raise TypeError("client must be an instance of Client")
		if not isinstance(message, str):
			raise TypeError("message must be an instance of str")
		self._notifyClient(client, message)