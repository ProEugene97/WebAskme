from django.core.management.base import BaseCommand
from question.models import Question, Profile, Tag, Answer
from django.contrib.auth.models import User
from datetime import datetime

class Command(BaseCommand):

	help = 'craete data for db'

	def handle(self):
		for i in range(10):
			user = User.objects.create_user(username='user' + str(i), password='user' + str(i + 1))
			user.save()
		for i in range(10):
			profile = Profile(user=User.objects.get(username='user' + str(i)), i, date(2005 + i, i + 1, (i + 1) * 2))
			profile.save()
		tags = ['django', 'python', 'shell', 'user', 'android', 'net', 'c', 'java', 'web', 'html']
		for i in tags:
			tag = Tag(title=i)
			tag.save()
		for i in range(10):
			q = Question(title="Cannot to set datetime with input field. Always return DateTime.MinValue", 
				text="My programm are supposed to have date filtr and gives article with proper date. But when i input any date in my datetime field my values don't change and are always DateTime.MinValue. Idk why and how i can fix it.",
				is_published=True,
				rating=i,
				author=Profile.objects.get(id=i + 1),
				likes=Profile.objects.get(id=(i + 2)//2),
				tags=Tag.objects.all()[:i]
				)
		for i in range(10):
			ans = Answer(text="Nice question!",
				added_at = date(2019, i + 1, (i + 1) * 2),
				question=Question.objects.get(id=i + 1),
				author=Profile.objects.get(id=(i + 2)//2),
				)
		for i in range(10):
			ans = Answer(text="I don't know!",
				added_at = date(2019, i + 2, i + 3),
				question=Question.objects.get(id=(i+2)//2),
				author=Profile.objects.get(id=(i+3)//2),
				)
