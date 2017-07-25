import sendgrid
SENDGRID_API_KEY='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'

import sendgrid

from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=(SENDGRID_API_KEY))
from_email = Email("khannapalak19@gmail.com")
to_email = Email("flickpalak@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)