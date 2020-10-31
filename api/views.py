from django.shortcuts import render, redirect

# Create your views here.

from .forms import NewBookForm
from myapi.models import Book
import requests

key = "AIzaSyCL4y-GYVZHATQMXDdbfFOMKT75-qtPFoY"

def book_create_view(request):
    form = NewBookForm(request.POST or None)
    if form.is_valid():
        title = request.POST.get('title')
        count = request.POST.get('count')
        print("Nikhil:", title, count)
        form.save()

    context = {
        'form': form
    }
    return render(request, 'index.html', context)

def books_list_view(request):
    form = NewBookForm(request.POST or None)
    if form.is_valid():
        title = request.POST.get('title')
        count = request.POST.get('count')
        print("Nikhil:", title, count)
        form.save()
        form = NewBookForm()

    context = {
        'form': form,
        'books': Book.objects.all()
    }

    return render(request, 'books_list.html', context)

def book_detail_view(request, my_id):
    obj = Book.objects.get(id=my_id)
    if request.GET.get('delete'):
        obj.delete()
        return redirect('/')
    if request.GET.get('update'):
        print(request.GET)


    context = {'book': obj}
    return render(request, 'book_detail.html', context)

# def search_view(request):
#     term = request.GET.get('term')
#     data = []
#     if term:
#         items = Item.objects.filter(value__icontains=term).values('value', 'id')
#         data = json.dumps(items)

#     return HttpResponse(data, content_type='application/json')
