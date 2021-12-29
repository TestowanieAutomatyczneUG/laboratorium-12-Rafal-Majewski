class Client:
	def _notify(self, message: str) -> None:
		print(message)
	def notify(self, message: str) -> None:
		if not isinstance(message, str):
			raise TypeError("message must be an instance of str")
		self._notify(message)