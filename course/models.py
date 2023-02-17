from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    career_path = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "courses"

    def __str__(self):
        return self.title


class Syllabus(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='syllabuses'
    )
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)

    class Meta:
        db_table = "syllabuses"

    def __str__(self):
        return self.title


class Project(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)

    class Meta:
        db_table = "projects"

    def __str__(self):
        return self.title
