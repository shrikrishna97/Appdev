from celery.schedules import crontab
from celery import Celery

app = Celery('myapp', broker='redis://localhost:6379/0')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Execute the task every day at a specific time in IST (e.g., 10:00 AM)
    sender.add_periodic_task(
        crontab(hour=10, minute=0, day_of_week='mon-fri'),
        send_daily_reminder.s()
    )

@app.task
def send_daily_reminder():
    # Your reminder logic here
    pass

