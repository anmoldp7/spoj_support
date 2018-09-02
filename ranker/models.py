from django.db import models
from django.utils import timezone

class user_handle(models.Model):
    handle_name = models.CharField(max_length = 50, primary_key = True)
    user_name = models.CharField(max_length = 50)
    user_location = models.CharField(max_length = 50)
    joining_date = models.CharField(max_length = 50)
    world_rank = models.IntegerField()
    points = models.FloatField()
    institution = models.TextField(max_length = 50)
    problems_solved = models.IntegerField()
    total_submissions = models.IntegerField()
    added_on = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return "<handle : {}, added_on : {}>".format(self.handle_name, self.added_on)