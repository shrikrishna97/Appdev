from celery import Celery
from reportlab.pdfgen import canvas
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

app = Celery('myapp', broker='redis://localhost:6379/0')

@app.task
def send_mail_with_pdf(email, pdf_data):
    msg = MIMEMultipart()
    msg['From'] = 'your_email@example.com'
    msg['To'] = email
    msg['Subject'] = 'Your PDF Report'

    msg.attach(MIMEText('Please find your report attached.'))

    pdf_file = MIMEApplication(pdf_data, 'pdf')
    pdf_file.add_header('Content-Disposition', 'attachment', filename='report.pdf')
    msg.attach(pdf_file)

    smtp = smtplib.SMTP('smtp.example.com', 587)
    smtp.starttls()
    smtp.login('your_email@example.com', 'your_password')
    smtp.sendmail('your_email@example.com', email, msg.as_string())
    smtp.quit()

