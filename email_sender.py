import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Ludah Makori'
email['to'] = 'ludahmaxs@gmail.com'
email['subject'] = 'You won 2,000,000 dollars!'


email.set_content('I am a Python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('lawmakori20@gmail.com','djludah*579')
    smtp.send_message(email)
