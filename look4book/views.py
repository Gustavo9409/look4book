from django.shortcuts import render, redirect
from . import services
from .forms import FormsBook
from django.contrib import messages

books_results = []

# This function initialize home page
# request: The request object used to generate this response.
# Returns the render of home template
def initHome(request): 
    global books_results
    
    context = {}
    if request.method == 'POST':
        form = FormsBook(request.POST)
        ev_ok = True
        if form.is_valid():
            author = form.cleaned_data["author_name"]
            book = form.cleaned_data["book_name"]
            check_author = form.cleaned_data["author_opt"]
            check_book = form.cleaned_data["book_opt"]

            if check_book == False and check_author == False:
                messages.info(request, 'You have to select a type of search.')
                ev_ok = False
            else:
                if book == "" and check_book == True:
                    messages.info(request, 'Enter the name of a Book')
                    ev_ok = False
                if author == "" and check_author == True:
                    messages.info(request, 'Enter the name of an Author')
                    ev_ok = False
            if ev_ok :
                book_list = services.get_books_by_param(book, author)
                for result in book_list: 
                    books_results.append(result)
                return redirect('Results')
    else:
        form = FormsBook()
    context = {'forms': form}
    return render(request, "look4book/index.html", context)

def showResults(request):
    global books_results
    context = {'books': books_results}
    books_results = []
    return render(request, "look4book/results.html", context)