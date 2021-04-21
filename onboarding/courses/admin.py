from django.contrib import admin
from .models import *

from django.contrib import admin
from django.db import models
from related_admin import RelatedFieldAdmin


@admin.register(Course)
class CourseAdmin(RelatedFieldAdmin):
    list_display = ('title', 'is_mandatory', 'status', 'type',)
    list_filter = ('title', 'is_mandatory', 'status', 'type',)
    search_fields = ('title', 'description',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish',)


@admin.register(Game)
class GameAdmin(RelatedFieldAdmin):
    list_display = ('course__title', 'course__is_mandatory', 'course__status',)
    list_filter = ('course__title', 'course__is_mandatory', 'course__status',)
    search_fields = ('course__title', 'course__description',)
    date_hierarchy = 'course__publish'
    ordering = ('course__status', 'course__publish',)


@admin.register(Document)
class DocumentAdmin(RelatedFieldAdmin):
    list_display = ('course__title', 'course__is_mandatory', 'course__status',)
    list_filter = ('course__title', 'course__is_mandatory', 'course__status',)
    search_fields = ('course__title', 'course__description',)
    date_hierarchy = 'course__publish'
    ordering = ('course__status', 'course__publish',)


@admin.register(Test)
class TestAdmin(RelatedFieldAdmin):
    list_display = ('course__title', 'max_attempts', 'course__is_mandatory', 'course__status',)
    list_filter = ('course__title', 'max_attempts', 'course__is_mandatory', 'course__status',)
    search_fields = ('course__title', 'course__description',)
    date_hierarchy = 'course__publish'
    ordering = ('course__status', 'course__publish',)


@admin.register(Question)
class QuestionAdmin(RelatedFieldAdmin):
    list_display = ('test__course__title', 'text', 'type',)
    list_filter = ('test__course__title', 'text', 'type',)
    raw_id_fields = ('test', )
    search_fields = ('test__course__title', 'text',)
    date_hierarchy = 'test__course__publish'
    ordering = ('test__course__title',)


@admin.register(Answer)
class AnswerAdmin(RelatedFieldAdmin):
    list_display = ('question__text', 'text', 'is_true',)
    list_filter = ('question__text', 'text', 'is_true',)
    raw_id_fields = ('question',)
    search_fields = ('question__text', 'text',)
    ordering = ('question__text',)



