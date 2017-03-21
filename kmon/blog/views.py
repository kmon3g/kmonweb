from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import Context,loader
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Entry 
from .models import Category
from .models import Photo
from .models import Comment
from .forms import PhotoForm
from .forms import CommentForm

def blog(request, category_title, page=1):
	category = get_object_or_404(Category, Title=category_title)
	ent = Entry.objects.filter(Category__Title=category_title).order_by('eid')
	paginator = Paginator(ent, 5)
	# Entries = Entry.objects.filter(Category__Title=category_title).order_by('eid')

	try:
		entries = paginator.page(page)
	except PageNotAnInteger:
		entries = paginator.page(1)
	except EmptyPage:
		entries = paginator.page(paginator.num_pages)

	context = ({
		'category' : category,
		'entries' : entries,
		})

	return render(request, 'blog.html', context)

def search(request, query):
	entries = Entry.objects.filter(Title__contains=query)
	# paginator = Paginator(ent, 5)

	# try:
	# 	entries = paginator.page(page)
	# except PageNotAnInteger:
	# 	entries = paginator.page(1)
	# except EmptyPage:
	# 	entries = paginator.page(paginator.num_pages)

	context = ({
		'entries' : entries,
		})
	return render(request, 'blog.html', context)

def read(request, category_title, entry_id):
	entry_id = int(entry_id)
	current_entry = get_object_or_404(Entry, eid=entry_id, Category__Title=category_title)
	category = get_object_or_404(Category, Title=category_title)
	comments = Comment.objects.filter(Entry__eid=entry_id, Entry__Category__Title=category_title)
	commentform = CommentForm()

	photos = Photo.objects.filter(Entry__eid=entry_id, Entry__Category__Title=category_title)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.Created = timezone.now()
			current_entry.Comments += 1
			current_entry.save()
			post.Entry = current_entry
			post.save()

	context = ({
		'entry' : current_entry,
		'photos' : photos,
		'comments' : comments,
		'content' : 'entry/%s_%s.html'%(category_title, entry_id),
		})

	return render(request, 'read.html', context)

def index(request):
	return render(request, 'index.html', {})


@login_required
def create(request):
	if request.method == "GET":
		form = PhotoForm()
	elif request.method == "POST":
		form = PhotoForm(request.POST, request.FILES)
		if form.is_valid():
			obj = edit_form.save(commit=False)
			obj.user = request.user
			obj = form.save()

			# return redirect('/admin')

	# template = loader.get_template('edit.html')
	context = {
		'form' : form ,
	}

	# return HttpResponse(template.render(context))
	return render(request, 'edit.html', context)