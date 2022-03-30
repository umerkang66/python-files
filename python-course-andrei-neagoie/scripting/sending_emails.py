import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# we want to customize the "$name" using Template
html = Template(Path('./htmls/index.html').read_text())
email = EmailMessage()
email["from"] = "Umer Gulzar <ugulzar4512@gmail.com>"
email["to"] = "ugulzar4512@gmail.com"
email["subject"] = "You won 1,000,000 dollars"
# we can do as keyword arguments {{name="Umer"}} or using dict
email.set_content(html.substitute({"name": "Umer"}), 'html')

with smtplib.SMTP(host="smtp-relay.sendinblue.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("{{SEND_IN_BLUE_EMAIL}}", "{{SEND_IN_BLUE_PASSWORD}}")
    smtp.send_message(email)
    print("All good boss!")
