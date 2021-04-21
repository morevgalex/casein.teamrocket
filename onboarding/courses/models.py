from django.db import models
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Course(models.Model):
    objects = models.Manager()
    published = PublishedManager()

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

    def get_absolute_url(self):
        return reverse('courses:course_detail', args=[self.slug])


class Game(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    game_src = models.URLField()


class Document(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Test(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    max_attempts = models.IntegerField(default=3)


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    TYPES = {
        ('single', 'Single'),
        ('multi', 'Multiple'),
    }
    text = models.CharField(max_length=500)
    type = models.CharField(max_length=10, choices=TYPES)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    text = models.CharField(max_length=500)
    is_true = models.BooleanField()

# TODO add trigger to db for checking of single answer

