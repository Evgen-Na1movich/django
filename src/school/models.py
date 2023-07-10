from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    group = models.ForeignKey(
        Group,
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='students'
    )
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.lastname}'


class Diary(models.Model):
    avg_score = models.DecimalField(max_digits=3, decimal_places=2)
    student = models.OneToOneField(
        'Student',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='students',
    )

    def __str__(self):
        return f"diary id{self.id}, student's name-{self.student.firstname}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    pages = models.SmallIntegerField(max_length=4)
    student = models.ManyToManyField(
        'Student',
        related_name='books',
        null=True, blank=True,
    )

    def __str__(self):
        return self.title
