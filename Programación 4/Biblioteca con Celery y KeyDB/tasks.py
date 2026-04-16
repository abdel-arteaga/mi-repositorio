from celery_app import celery
from flask_mail import Message
from app import create_app
from app.extensions import mail
import os

@celery.task(bind=True, max_retries=3)
def send_email(self, subject, recipient, body):
    try:
        app = create_app()

        with app.app_context():
            msg = Message(
                subject=subject,
                sender=os.getenv('MAIL_USERNAME'),
                recipients=[recipient]
            )
            msg.body = body

            mail.send(msg)

    except Exception as e:
        raise self.retry(exc=e, countdown=10)