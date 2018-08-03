from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from home.forms import HomeForm,CommentForm
#from home.models import Post
from .models import Post, Comment



class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()

        posts = Post.objects.all().order_by('-created')

        args = {'form': form, 'posts': posts}
        return render(request, self.template_name , args)


    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user

            post.save()


            text = form.cleaned_data['post']

            form = HomeForm()
            return redirect('home:home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


    def get_comment(self, request):
        form = CommentForm()
        posts = Post.objects.all().order_by('-created')

        args = {'form': form, 'posts': posts}
        return render(request, 'home/comment.html' , args)

    def post_comment(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            texts = form.save(commit=False)
            texts.user = request.user
            texts.save()

            text = form.cleaned_data['texts']
            form = CommentForm()
            return redirect('home:home')

        args = {'form': form, 'text': text}
        return render(request, 'home/comment.html', args)



    '''def add_comment(self, request):
        post = Post.objects.all()
        if request.method == "POST":
            form = HomeForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('/home')
        else:
            form = CommentForm()
        return render(request, 'home/comment.html', {'form': form})

    def post_edit(self,request):
        #print(pk)
        #print(type(pk))
        #post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('home:home')
        else:
            form = PostForm(instance=post)
        return render(request, 'home/post_edit.html', {'form': form})'''