from modules.MailServer import MailServer
from modules.Messenger import Messenger
from modules.TemplateEngine import TemplateEngine
import unittest
from unittest.mock import patch

class Test_Messenger(unittest.TestCase):
	def setUp(self):
		self.templateEngine = TemplateEngine()
		self.mailServer = MailServer()

	def test_receiveMessage(self):
		messenger1 = Messenger(templateEngine=self.templateEngine, mailServer=self.mailServer)
		messenger2 = Messenger(templateEngine=self.templateEngine, mailServer=self.mailServer)
		with patch.object(messenger2, "receiveMessage") as mock_messenger2_receiveMessage:
			with patch.object(self.templateEngine, "applyTemplate", side_effect=lambda text: {"text": text}):
				with patch.object(self.mailServer, "receiveMessage", side_effect=lambda sender, recipient, message: recipient.receiveMessage(sender, message)):
					messenger1.sendText(messenger2, "Hello world!")
					mock_messenger2_receiveMessage.assert_called_once_with(messenger1, {"text": "Hello world!"})

	def test_sendText_if_uses_mailServer(self):
		messenger = Messenger(templateEngine=self.templateEngine, mailServer=self.mailServer)
		with patch.object(self.templateEngine, "applyTemplate", side_effect=lambda text: {"text": text}):
			with patch.object(self.mailServer, "receiveMessage", side_effect=lambda sender, recipient, message: recipient.receiveMessage(sender, message)) as mock_mailServer_receiveMessage:
				messenger.sendText(messenger, "Hello world!")
				mock_mailServer_receiveMessage.assert_called_once_with(messenger, messenger, {"text": "Hello world!"})

	def test_sendText_if_raises_TypeError_if_recipient_is_not_Messenger(self):
		messenger = Messenger(templateEngine=self.templateEngine, mailServer=self.mailServer)
		with self.assertRaises(TypeError):
			messenger.sendText(object(), "Hello world!")

	def test_sendText_if_raises_TypeError_if_text_is_not_str(self):
		messenger = Messenger(templateEngine=self.templateEngine, mailServer=self.mailServer)
		with self.assertRaises(TypeError):
			messenger.sendText(messenger, object())

	def test_sendText_if_applies_template(self):
		messenger = Messenger(templateEngine=self.templateEngine, mailServer=self.mailServer)
		with patch.object(self.templateEngine, "applyTemplate") as mock_applyTemplate:
			try:
				messenger.sendText(messenger, "Hello world!")
			except:
				pass
			mock_applyTemplate.assert_called_once_with("Hello world!")
