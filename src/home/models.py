from django.db import models


class Cases(models.Model):
    name = models.CharField(max_length=128)
    students_reported = models.IntegerField()
    students_recovered = models.IntegerField()
    students_active = models.IntegerField()
    faculty_reported = models.IntegerField()
    faculty_recovered = models.IntegerField()
    faculty_active = models.IntegerField()
    total_reported = models.IntegerField()
    total_recovered = models.IntegerField()
    total_active = models.IntegerField()
    report_date = models.CharField(max_length=128)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Case"
        verbose_name_plural = "Cases"

    @property
    def title(self):
        return self.name