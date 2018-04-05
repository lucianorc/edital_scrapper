"""Email Sender."""
from decouple import config
import requests
import os


class EmailSender():

    """Email Sender class."""

    def __init__(self, user, email):
        """Email Sender constructor."""
        self.user = user
        self.email = email
        self.domain = config('MAILGUN_DOMAIN')
        self.api_key = config('MAILGUN_KEY')

    def send(self):
        """Sender method."""
        from_email = f"postmaster@{self.domain}"
        template_path = os.path.join(
            os.getcwd(),
            "edital_scrapper/senders/templates/email.html"
        )

        with open(template_path, 'r') as template:
            return requests.post(
                f"https://api.mailgun.net/v3/{self.domain}/messages",
                auth=("api", self.api_key),
                data={
                    "from": f"Edital Scrapper <{from_email}>",
                    "to": f"{self.user} <{self.email}>",
                    "subject": f"Hello, {self.user}",
                    "text": template.read().format(user=self.user)
                }
            )
