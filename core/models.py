from django.db import models
from django.shortcuts import reverse


class Student(models.Model):
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество', blank=True)
    birthday = models.DateField(verbose_name='Дата рождения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True, null=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, verbose_name='Группа')

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic} {self.group}'

    def get_absolute_url(self):
        return reverse('student', kwargs={'student_id': self.pk})

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['group', 'surname']


class Group(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название группы')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('group', kwargs={'group_id': self.pk})

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['name']


class Discipline(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название предмета')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('discipline', kwargs={'discipline_id': self.pk})


class Mark(models.Model):
    MARKS = (
        ('fail', 'незачет'),
        ('pass', 'зачет'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    value = models.CharField(max_length=5, choices=MARKS, null=True)
    date = models.DateTimeField(auto_now=True, verbose_name='Дата оценивания')
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, verbose_name='Предмет')
    student = models.ForeignKey('Student', on_delete=models.CASCADE, verbose_name='Студент')

    def __str__(self):
        return f'{self.student} - {self.discipline} - {self.value}'

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
