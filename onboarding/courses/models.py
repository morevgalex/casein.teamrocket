from django.db import models
from django.utils import timezone


class Course(models.Model):
    STATUS_CHOICES = {
        ('draft', 'Draft'),
        ('published', 'Published'),
    }

    TYPES = {
        ('test', 'Test'),
        ('game', 'Game'),
        ('doc', 'Document'),
    }

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    is_mandatory = models.BooleanField(default=False)
    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    type = models.CharField(max_length=10, choices=TYPES)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Game(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    game_src = models.URLField()


class Document(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Test(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


