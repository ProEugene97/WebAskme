from django.shortcuts import render
from django.http import Http404
from question import models
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.urls import reverse 

def paginate(request, qs):
	try:
		limit = int(request.GET.get('limit', 5))
	except ValueError:
		limit = 5
	if limit < 0 or limit > 100:
		limit = 5
	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		page = 1
	except TypeError:
		page = 1
	paginator = Paginator(qs, limit)
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return (page, paginator)

def get_main_page(request):
	try:
		questions = models.Question.objects.new()
	except models.Question.DoesNotExist:
		raise Http404
	page, paginator = paginate(request, questions)
	paginator.baseurl = "%s?page=" % reverse('main')
	return render(request, "main.html", {
		"questions":page,
		"page": page,
		"paginator": paginator,})

def get_question_page(request, num):
	try:
		question = models.Question.objects.get(id=num)
	except models.Question.DoesNotExist:
		raise Http404
	return render(request, "question.html", {"question":question,})    

def get_login_page(request):
    return render(request, "login.html", )

def get_signup_page(request):
    return render(request, "signup.html", )

def get_ask_page(request):
    return render(request, "ask.html", )

def get_hot_page(request):
	try:
		questions = models.Question.objects.hot()
	except models.Question.DoesNotExist:
		raise Http404
	page, paginator = paginate(request, questions)
	paginator.baseurl = "%s?page=" % reverse('hot')
	return render(request, "hot.html", {
		"questions":page,
		"page": page,
		"paginator": paginator,})

def get_tag_page(request, title):
	try:
		questions = models.Question.objects
		tag = models.Tag.objects.get(title=title)
	except models.Tag.DoesNotExist:
		raise Http404
	page, paginator = paginate(request, tag.question_set.all())
	paginator.baseurl = "%s?page=" % reverse('tag', args=[tag.title])
	return render(request, "tag.html", {
		"tag":tag,
		"questions": page,
		"page": page,
		"paginator": paginator,})
