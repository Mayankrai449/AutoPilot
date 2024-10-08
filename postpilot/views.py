from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import ScheduledPost
from .forms import ScheduledPostForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

@login_required
def dashboard(request):
    posts = ScheduledPost.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'posts': posts})

@csrf_exempt
def schedule_post(request):
    if request.method == 'POST':
        form = ScheduledPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.user = request.user
            else:
                post.user = None
            post.save()
            
            messages.success(request, 'Post scheduled successfully!')
            return HttpResponse('Post Scheduled!')
        else:
            messages.error(request, 'Form submission failed. Please correct the errors below.')
    else:
        form = ScheduledPostForm()
        
    return render(request, 'schedule_post.html', {'form': form})


@login_required
def post_list(request):
    posts = ScheduledPost.objects.filter(user=request.user).order_by('-scheduled_time')
    
    return render(request, 'post_list.html', {'posts': posts})

@login_required
def edit_post(request, post_id):
    post = ScheduledPost.objects.get(id=post_id, user=request.user)
    if request.method == 'POST':
        form = ScheduledPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Post updated successfully!')
            return redirect('post_list')
    else:
        form = ScheduledPostForm(instance=post)
        
    return render(request, 'edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, post_id):
    post = ScheduledPost.objects.get(id=post_id, user=request.user)
    post.delete()
    
    messages.success(request, 'Post deleted successfully!')
    return redirect('post_list')