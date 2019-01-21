from django.shortcuts import render,get_object_or_404,redirect


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.views import generic

from . import models
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


# VIEWS RELATED TO POST CREATE, LIST, DELETE, DETAIL, USER LIST
class CreatePost(LoginRequiredMixin, generic.CreateView):
    model = models.Post
    fields = ['title','message']


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostList(generic.ListView):
    model = models.Post
    ####


class PostDetail(LoginRequiredMixin,generic.DetailView):
    model = models.Post

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )


class DeletePost(LoginRequiredMixin, generic.DeleteView):
    model = models.Post
    success_url = reverse_lazy("blog:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)


class UserPosts(LoginRequiredMixin,generic.ListView):
    model = models.Post
    template_name = "blog/user_post_list.html"

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("posts").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context



# VIEWS RELATED TO COMMENTS

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(models.Post,pk=pk)

    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user.username
            comment.save()
            # return redirect ('post_detail',pk=post.pk)
            return redirect ('blog:single',pk=post.pk,username=post.user.username)
    else:
        form = forms.CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})