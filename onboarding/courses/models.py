from django.db import models
from django.db.models import CheckConstraint, Q, Subquery
from django.utils import timezone


class CourseType(models.IntegerChoices):
    TEST = 1, "Test"
    GAME = 2, "Game"
    DOCUMENT = 3, 'Document'


class Course(models.Model):
    STATUS_CHOICES = {
        ('draft', 'Draft'),
        ('published', 'Published'),
    }

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    is_mandatory = models.BooleanField(default=False)
    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    type = models.IntegerField(choices=CourseType.choices)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class GameCourseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=CourseType.GAME)


class GameCourse(Course):
    objects = GameCourseManager()
    game_src = models.URLField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = CourseType.GAME

    class Meta:
        proxy = True


class DocumentCourseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=CourseType.DOCUMENT)


class DocumentCourse(Course):
    objects = GameCourseManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = CourseType.DOCUMENT

    class Meta:
        proxy = True


class TestCourseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=CourseType.TEST)


class TestCourse(Course):
    objects = GameCourseManager()
    max_attempts = models.IntegerField(default=3)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = CourseType.TEST

    class Meta:
        proxy = True


class Question(models.Model):
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
