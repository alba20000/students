from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from core import models


class Index(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students = models.Student.objects.all()
        groups = models.Group.objects.all()
        disciplines = models.Discipline.objects.all()
        count = models.Student.objects.count()
        context['students'] = students
        context['groups'] = groups
        context['disciplines'] = disciplines
        context['count'] = count
        return context


class Discipline(TemplateView):
    template_name = 'core/discipline.html'

    def get_context_data(self, discipline_id, **kwargs):
        context = super().get_context_data(**kwargs)
        marks = models.Mark.objects.filter(discipline=discipline_id)
        discipline = models.Discipline.objects.get(pk=discipline_id)
        context['marks'] = marks
        context['discipline'] = discipline
        return context


class Group(TemplateView):
    template_name = 'core/group.html'

    def get_context_data(self, group_id, **kwargs):
        context = super().get_context_data(**kwargs)
        students = models.Student.objects.filter(group=group_id)
        group = models.Group.objects.get(pk=group_id)
        context['students'] = students
        context['group'] = group
        return context


class Student(TemplateView):
    template_name = 'core/student.html'

    def get_context_data(self, student_id, **kwargs):
        context = super().get_context_data(**kwargs)
        marks = models.Mark.objects.filter(student=student_id)
        student = models.Student.objects.get(pk=student_id)
        context['marks'] = marks
        context['student'] = student
        return context
