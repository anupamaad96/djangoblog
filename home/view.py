from home.forms import HomeForm,CommentForm

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