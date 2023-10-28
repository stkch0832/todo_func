from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator
from django.contrib import messages


def post_lists(request):
    post_item = Post.objects.all().order_by('-updated_at')
    paginator = Paginator(post_item, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app/post_lists.html', context= {
        'page_obj': page_obj,
    })


def post_detail(request, pk):
    post_data = get_object_or_404(Post, pk=pk)
    return render(request, 'app/post_detail.html', context={
        'post_data': post_data,
    })


def post_create(request):
    form = PostForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            post_data = Post()
            post_data.user = request.user
            post_data.title = form.cleaned_data['title']
            post_data.status = form.cleaned_data['status']
            post_data.deadline = form.cleaned_data['deadline']
            post_data.description = form.cleaned_data['description']

            post_data.save()
            messages.success(request, '新規作成が完了しました。')
            return redirect('app:post_lists')

    else:
        form = PostForm()

    return render(request, 'app/post_form.html', context={
        'form': form,
    })


def post_edit(request, pk):
    post_data = get_object_or_404(Post, pk=pk)

    if post_data.user_id != request.user.id:
        return HttpResponseForbidden("権限がありません")

    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            post_data.title = form.cleaned_data['title']
            post_data.status = form.cleaned_data['status']
            post_data.deadline = form.cleaned_data['deadline']
            post_data.description = form.cleaned_data['description']

            post_data.save()
            messages.success(request, '更新が完了しました。')
            return redirect('app:post_lists')
    else:
        form =PostForm(
            request.POST or None,
            initial={
                'title': post_data.title,
                'status': post_data.status,
                'deadline': post_data.deadline,
                'description': post_data.description,
            })

    return render(request, 'app/post_form.html', context={
        'form': form,
    })


def post_delete(request, pk):
    post_data = get_object_or_404(Post, pk=pk)

    if post_data.user_id != request.user.id:
        return HttpResponseForbidden("権限がありません")

    if request.method == 'POST':
        post_data.delete()
        messages.error(request, 'タスクを削除しました')
    return redirect('app:post_lists')
