from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
#from django.http import HttpResponseRedirect

# Create your views here.
def Abdalla(request):
    if request.method == 'POST':
        add_book = Loginform(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_category = Login(request.POST)
        if add_category.is_valid():
            add_category.save()

    context = {
        's':Category.objects.all(),
        'a':Book.objects.all(),
        'er':Loginform(),
        'es':Login(),
        "all_boos":Book.objects.filter(active=True).count(),
        "all_boos_solid":Book.objects.filter(status='solid').count(),
        "all_boos_rental":Book.objects.filter(status='rental').count(),
        "all_boos_valiable":Book.objects.filter(status='available').count(),
}
    return render(request, 'pages/index.html',context)

def Omer(request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title :
            search = search.filter(title__icontains = title)

            

    if request.method == 'POST':
        add_category = Login(request.POST)
        if add_category.is_valid():
            add_category.save()

    contexts = {
        's':Category.objects.all(),
        'a': search,
        'er':Loginform(),
        'es':Login(),
    }
    return render(request, 'pages/book.html',contexts)

def fatma(request,id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = Loginform(request.POST,request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = Loginform(instance = book_id)
    contextes = {
        'you':book_save,
    }
    return render(request,'pages/update.html',contextes)


def abdelrahman(request,id):
    book_del = get_object_or_404(Book, id = id)
    if request.method == 'POST':
        book_del.delete()
        return redirect('/')
    return render(request, 'pages/delate.html')


