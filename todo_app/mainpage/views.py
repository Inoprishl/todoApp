from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from todo.models import TodoModel

# Create your views here.

def tasks_view(request, *args, **kwargs):
    task = TodoModel.objects.all()
    paginator = Paginator(task, 4)
    page = paginator.get_page(request.GET.get('page')) if request.GET.get('page') else paginator.get_page(1)
    done = True if task.filter(status=True) else False
    return render(request, 'mainpage/tasks.html', {'pag': paginator, 'p': page, 'd':done}) 
    done = TodoModel.objects.filter(status=True)
    if task:
        is_done = True if done else False    
        paginator = Paginator(task, 4)
        if request.GET.get('page'):
            page = request.GET.get('page')
            foo = paginator.page(page) 
            currentPage = foo.object_list
            is_first = foo.has_previous()
            previous_page = int(page)-1
            is_last = foo.has_next()
            next_page = int(page)+1
            last_page = paginator.num_pages
            context = {'page': currentPage,'is_first': is_first, 'is_last': is_last,'previous_page': previous_page, 'next_page': next_page, 'page_num': page, 'last_page': last_page, 'is_done': is_done}
            return render(request, 'mainpage/tasks.html', context)
        context = {'page': paginator.page(1).object_list, 'is_first': False, 'is_last': True, 'previous_page': 0, 'next_page': 2, 'page_num': 1, 'last_page': paginator.num_pages, 'is_done': is_done}
        return render(request, 'mainpage/tasks.html', context) 
    return redirect('/')
