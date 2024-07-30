from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ScheduledPost
from .forms import ScheduledPostForm
from django.contrib import messages

@login_required
def dashboard(request):
    posts = ScheduledPost.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'posts': posts})


@login_required
def schedule_post(request):
    if request.method == 'POST':
        form = ScheduledPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Post scheduled successfully!')
            return redirect('post_list')
    else:
        form = ScheduledPostForm()
    return render(request, 'post_scheduler/schedule_post.html', {'form': form})
