from django.shortcuts import render, redirect
from . import services
from .forms import FormsBook
from django.contrib import messages

books_results = [{'title':'El señor de los anillos'}]

# This function initialize home page
# request: The request object used to generate this response.
# Returns the render of home template
def initHome(request): 
    context = {}
    if request.method == 'POST':
        form = FormsBook(request.POST)
        if form.is_valid():
            author = form.cleaned_data["book_name"]
            book = form.cleaned_data["author_name"]
 
            book_list = services.get_books_by_id()
            return redirect('Results')
    else:
        form = FormsBook()
    context = {'forms': form}
    return render(request, "look4book/index.html", context)

def showResults(request):
    context = {'books': books_results}
    return render(request, "look4book/results.html", context)