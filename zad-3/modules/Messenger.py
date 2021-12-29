from modules.TemplateEngine import TemplateEngine
from modules.MailServer import MailServer


class Messenger:
	def __init__(self, *, templateEngine: TemplateEngine, mailServer: MailServer):
		self.templateEngine = templateEngine
		self.mailServer = mailServer
	def receiveMessage(self, sender, message):
		pass
	def sendText(self, recipient, text):
		if not isinstance(recipient, Messenger):
			raise TypeError("recipient must be Messenger")
		if not isinstance(text, str):
			raise TypeError("text must be str")
		self.mailServer.receiveMessage(self, recipient, self.templateEngine.applyTemplate(text))
