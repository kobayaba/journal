from django.shortcuts import render
from django.views.generic import (
	ListView,
	DetailView,
	DeleteView,
	UpdateView,
	CreateView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	UserPassesTestMixin,
)

from .models import Article

class ArticleListView(LoginRequiredMixin, ListView):
	model = Article
	login_url = 'login'
	template_name = 'article_list.html'

class ArticleDetailView(LoginRequiredMixin, DetailView):
	model = Article
	login_url = 'login'
	template_name = 'article_detail.html'


class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model = Article
	fields = ['title', 'body']
	login_url = 'login'
	template_name = 'article_edit.html'

	def test_func(self):
		obj = self.get_object()
		return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Article
	login_url = 'login'
	template_name = 'article_delete.html'

	success_url = reverse_lazy('article_list')

	def test_func(self):
		obj = self.get_object()
		return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
	model = Article
	template_name = 'article_new.html'
	fields = ('title', 'body', )
	login_url = 'login'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

