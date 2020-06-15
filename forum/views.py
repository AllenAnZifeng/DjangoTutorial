from django.shortcuts import render, redirect, reverse
from .models import ForumUser, Threads, Comments, Posts
from .forms import ThreadForm, PostForm, ForumUserForm
import pprint
from django.contrib.auth.decorators import login_required

# Create your views here.

pp = pprint.PrettyPrinter(indent=4)


def home(request):
    threads = Threads.objects.all()
    for thread in threads:
        if len(thread.content) > 50:
            thread.content = thread.content[:50]
            thread.content += ' ... ...'

    if request.method == 'POST':
        try:
            forum_user = request.user.forum_user
            forum_user.picture = request.FILES['picture']
            forum_user.save()
        except Exception as e:
            print(e)

            return redirect('forum:home')

    context = {'threads': threads}
    return render(request, 'forum/home.html', context)


@login_required(login_url='authentication:login')
def create_thread(request):
    form = ThreadForm()

    if request.method == 'POST':
        form = ThreadForm(request.POST)
        print(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)  # type: Threads
            thread.author = request.user.forum_user
            thread.save()
            return redirect('forum:home')

    context = {'form': form, }
    return render(request, 'forum/createThread.html', context)


@login_required(login_url='authentication:login')
def create_post(request, pk):
    form = PostForm()
    thread = Threads.objects.get(pk=pk)
    posts = thread.posts.all()

    if request.method == 'POST':
        form = PostForm(request.POST)
        print(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # type: Posts
            post.author = request.user.forum_user
            post.thread = thread
            post.save()
            return redirect('forum:createPost', pk=pk)

    context = {'form': form, 'thread': thread, 'posts': posts}
    return render(request, 'forum/createPost.html', context)


@login_required(login_url='authentication:login')
def create_comment(request, pk):
    if request.method == 'POST':
        print(pk)

        content = request.POST['Comment']
        post = Posts.objects.get(pk=int(pk))
        thread_id = post.thread.id
        author = request.user.forum_user
        print(content, post, author)
        comment = Comments(author=author, post=post, content=content)
        comment.save()

        return redirect('forum:createPost', pk=thread_id)

    return redirect('forum:home')


def activate(request):
    user = request.user
    if user.is_authenticated:
        forumUser = ForumUser(user=user)
        forumUser.save()
        return redirect('forum:home')
    else:
        return redirect('authentication:register')


@login_required(login_url='authentication:login')
def profile(request, pk):
    user = ForumUser.objects.get(pk=pk)
    threads = user.threads.all()
    posts = user.posts.all()
    comments = user.comments.all()

    context = {'threads': threads, 'posts': posts, 'comments': comments}

    return render(request, 'forum/profile.html', context)
