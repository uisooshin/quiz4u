from django.conf import settings
from django.db import models
from django.utils import timezone

class Quiz(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    quiz_number = models.AutoField(primary_key=True)

    title = models.CharField(max_length=200)
    quiz_contents = models.TextField()

    example1 = models.TextField()
    example2 = models.TextField()
    example3 = models.TextField()
    example4 = models.TextField()
    correct = models.IntegerField()

    subject = models.TextField()
    detail_subject = models.TextField()

    bookmark_count = models.IntegerField()
    correct_count = models.IntegerField()
    wrong_count = models.IntegerField()


    reveal_date = models.DateTimeField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
