from django.db import models
from django.contrib.auth.models import User

# Event Model
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    registration_limit = models.IntegerField()

    def __str__(self):
        return self.title

# Attendance Model
class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    check_in = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username} - {self.event.title}"

# Feedback Model (optional)
class Feedback(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
