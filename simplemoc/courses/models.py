import os
from django.db import models
from django.urls import reverse


# Create your models here.
class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(descripton__icontains=query)
        )

class Courses(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    descripton = models.TextField('Descricao Simples, blank=True')
    about = models.TextField('Sobre o curso', blank=True)
    start_date = models.DateField('data de inicio', null=True, blank=True)
    image = models.ImageField(upload_to='couses/image', verbose_name='imagem', null=True, blank=True)

    created_at = models.DateTimeField('criado em', auto_now_add=True)

    updated_at = models.DateTimeField('atualizado em', auto_now_add=True)

    objects = CourseManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('courses:details', args=[self.slug])

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']