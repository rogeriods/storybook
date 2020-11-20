from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from storybook.models import Story
from storybook.forms import StoryForm


class StoryListView(ListView):
    model = Story
    paginate_by = 5
    ordering = ['-id']


class StoryCreate(CreateView):
    model = Story
    form_class = StoryForm
    template_name = 'storybook/story_form.html'
    # fields = ['title', 'text']


class StoryUpdate(UpdateView):
    model = Story
    form_class = StoryForm
    template_name = 'storybook/story_form.html'
    # fields = ['title', 'text']


class StoryDelete(DeleteView):
    model = Story
    success_url = reverse_lazy('story-list')
    template_name = 'storybook/story_confirm_delete.html'
