from django.db import models
from datetime import datetime
from django.urls import reverse 
from django.contrib.auth.models import User


class Profile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')

	rating = models.IntegerField(default=0, verbose_name='Рейтинг')

	birthday = models.DateField(verbose_name='День рождения')

	#avatar = models.ImageField(upload_to = 'media', verbose_name='Аватарка')

	def __str__(self):
		return '{}_{}'.format(self.user, self.rating)


	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'



class Tag(models.Model):
        
	title = models.TextField(unique=True, default="", verbose_name='Название')

	def __str__(self):
	    return self.title

	def get_url(self):
	    return reverse('tag', args=[self.title])

	class Meta:
		verbose_name = 'Тэг'
		verbose_name_plural = 'Теги'




class QuestionManager(models.Manager):


	def hot(self):
		return self.filter(rating__gt=1, )


	def new(self):
		return self.filter(
			is_published=True,
			date_published__lt=datetime.now()).order_by('-date_published')




class Question(models.Model): 
    
	title = models.CharField(max_length=255, verbose_name='Заголовок')
	text = models.TextField(default="", verbose_name='Текст')
	date_published = models.DateTimeField(verbose_name='Дата публикации')
	is_published = models.BooleanField(verbose_name='Опубликовано')
	#added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(Profile, related_name='authors', null=True, on_delete=models.SET_NULL)
	likes = models.ManyToManyField(Profile, verbose_name='Лайки')
	tags = models.ManyToManyField(Tag, verbose_name='Тэги')

	objects = QuestionManager()

	def __str__(self):
	    return self.title

	def get_url(self):
	    return "/question/{}/".format(self.id)

	class Meta:
	    verbose_name = 'Вопрос'
	    verbose_name_plural = 'Вопросы'
	    index_together = [('title', 'text')]
	    unique_together = [('title', 'text')]


class Answer(models.Model):
        
	text = models.TextField(default="", verbose_name='Текст')
	added_at = models.DateField(null=True, verbose_name='Дата публикации')
	question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL, verbose_name='Вопрос')
	author = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL, verbose_name='Автор')

	def __str__(self):
	    return self.text

	class Meta:
		verbose_name = 'Ответ'
		verbose_name_plural = 'Ответы'
