from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ScheduledPost
from .forms import ScheduledPostForm


@login_required
def dashboard(request):
    posts = ScheduledPost.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'posts': posts})


@login_required
def schedule_post(request):
    if request.method == 'POST':
        form = ScheduledPostForm(request.POST, request.FILES)
        if form.is_valid():
            scheduled_post = form.save(commit=False)
            scheduled_post.user = request.user
            scheduled_post.save()
            return redirect('dashboard')
    else:
        form = ScheduledPostForm()
    return render(request, 'schedule_post.html', {'form': form})
