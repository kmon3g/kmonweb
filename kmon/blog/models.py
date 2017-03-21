from django.db import models
from django.utils import timezone
from django.conf import settings
# from django import forms
# Create your models here.

class Category(models.Model):
	#카테고리 명
	Title = models.CharField(max_length=40, null=False)

	Image_File = models.ImageField(upload_to='/category/', null=True)

	def __str__(self): 
		return self.Title

class TagModel(models.Model):
	#태그 명
	Title = models.CharField(max_length=20, null=False)

	def __str__(self):
		return self.Title

class Entry(models.Model):
	eid = models.PositiveIntegerField(default=1, null=False)
	#작성자
	User = models.ForeignKey(settings.AUTH_USER_MODEL)
	#글 제목	
	Title = models.CharField(max_length=80, null=False)
	#글 본문	
	Content = models.TextField(max_length=2000, null=False)
	#작성 일시	
	Summary = models.TextField(max_length=500, null=False)
	#미리보기
	Created = models.DateTimeField(default=timezone.now)
	#카테고리
	Category = models.ForeignKey(Category)
	#태그	
	Tags = models.ManyToManyField(TagModel, null=True)
	#댓글 수
	Comments = models.PositiveIntegerField(default=0, null=True)

	def __str__(self): 
		return '%s_%s' % (self.Category.Title , self.eid) 

class Photo(models.Model):
	pid = models.PositiveIntegerField(default=1, null=False)

	Entry = models.ForeignKey(Entry)

	Image_File = models.ImageField(upload_to='/image/%Y/%m/%d')

	# Filtered_Image_File = models.ImageField(upload_to='kmon/uploaded/filtered/%Y/%m/%d')

	Description = models.TextField(max_length=500, blank=True)

	Created = models.DateTimeField(default=timezone.now)

	def delete(self, *args, **kwargs):
		self.Image_File.delete()
		self.Filtered_Image_File.delete()
		super(Photo, self).delete(*args , **kwargs)

	def __str__(self): 
		return '%s_%s_%s' % (self.Entry.Category.Title, self.Entry.eid , self.pid) 


class Comment(models.Model):
	#댓글 작성자
	Name = models.CharField(max_length=20, null=False)
	#댓글 비밀번호
	Password = models.CharField(max_length=32, null=False)
	#댓글내용
	Content = models.TextField(max_length=2000, null=False)
	#작성 일시
	Created = models.DateTimeField(default=timezone.now)
	#댓글단 글
	Entry = models.ForeignKey(Entry)

	def __str__(self):
		return self.Name 