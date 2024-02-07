from django.db import models

# Create your models here.
class InternshipApplication(models.Model):
    ojt_duration = models.IntegerField()
    province = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    school_address = models.CharField(max_length=255)

    class Meta:
        db_table = 'InternshipApplication'