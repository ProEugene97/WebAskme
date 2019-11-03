from django.core.management.base import BaseCommand
from question.models import Question, Profile, Tag, Answer
from django.contrib.auth.models import User
from datetime import datetime, date, time

class Command(BaseCommand):

	help = 'craete data for db'

	def handle(sself, *args, **options):
		for i in range(10):
			try:
				user = User.objects.get(username='user'+str(i))
			except User.DoesNotExist:
				user = User.objects.create_user(username='user' + str(i), password='user' + str(i + 1))
				user.is_superuser=False
				user.is_staff=False
				user.save()

		for i in range(10):
			try:
				profile = Profile.objects.get(user=User.objects.get(username='user' + str(i)))
			except Profile.DoesNotExist:
				profile = Profile(user=User.objects.get(username='user' + str(i)), rating=i, birthday=date(2005 + i, i + 1, (i + 1) * 2))
				profile.save()

		tags = ['django', 'python', 'shell', 'user', 'android', 'net', 'c', 'java', 'web', 'html']
		for i in tags:
			try:
				tag = Tag.objects.get(title=i)
			except Tag.DoesNotExist:	
				tag = Tag(title=i)
				tag.save()

		for i in range(10):
			try:
				q = Question.objects.get(title="Cannot to set datetime with input field. Always return DateTime.MinValue" + str(i), 
				text= str(i) + "My programm are supposed to have date filtr and gives article with proper date. But when i input any date in my datetime field my values don't change and are always DateTime.MinValue. Idk why and how i can fix it.",
				is_published=True,
				author=Profile.objects.get(id=i + 1),
				)
			except Question.DoesNotExist:
				q = Question(title="Cannot to set datetime with input field. Always return DateTime.MinValue" + str(i), 
					text=str(i) +"My programm are supposed to have date filtr and gives article with proper date. But when i input any date in my datetime field my values don't change and are always DateTime.MinValue. Idk why and how i can fix it.",
					date_published = datetime.now(),
					is_published=True,
					rating=i,
					author=Profile.objects.get(id=i + 1),
					#likes=likes.set(Profile.objects.get(id=(i + 2)//2)),
					#tags=Tag.objects.get(id=i+1)
					)
				#q.likes.set(Profile.objects.get(id=(i + 2)//2))
				#q.tags.set(Tag.objects.get(id=i+1))
				q.save()
				q.likes.add(Profile.objects.get(id=(i + 2)//2))
				q.tags.add(Tag.objects.get(id=i+1))

		for i in range(10):
			try:
				ans = Answer.objects.get(text="Nice question!",
				added_at = date(2019, i + 1, (i + 1) * 2),
				question=Question.objects.get(id=i + 1),
				author=Profile.objects.get(id=(i + 2)//2),
				)
			except Answer.DoesNotExist:
				ans = Answer(text="Nice question!",
					added_at = date(2019, i + 1, (i + 1) * 2),
					question=Question.objects.get(id=i + 1),
					author=Profile.objects.get(id=(i + 2)//2),
					)
				ans.save()

		for i in range(10):
			try:
				ans = Answer.objects.get(text="I don't know!",
				added_at = date(2019, i + 2, i + 3),
				question=Question.objects.get(id=(i+2)//2),
				author=Profile.objects.get(id=(i+3)//2),
				)
			except Answer.DoesNotExist:
				ans = Answer(text="I don't know!",
					added_at = date(2019, i + 2, i + 3),
					question=Question.objects.get(id=(i+2)//2),
					author=Profile.objects.get(id=(i+3)//2),
					)
				ans.save()
