from django.db import models

# Create your models here.
class InternshipApplication(models.Model):
    id = models.IntegerField(primary_key=True)
    ojt_duration = models.IntegerField()
    province = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    school_address = models.CharField(max_length=255)

    def __str__(self):
        return f"InternshipApplication {self.id}"
