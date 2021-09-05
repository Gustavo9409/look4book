from django.shortcuts import render, redirect
from . import services
from .forms import FormsBook
from django.contrib import messages

books_results = [{'title':'El señor de los anillos', 'authors':["JRR TOkien","Gustavo"],"publish_date":"1974","number_of_pages":"440","identifier_OL":"OL88899"}]

# This function initialize home page
# request: The request object used to generate this response.
# Returns the render of home template
def initHome(request): 
    context = {}
    if request.method == 'POST':
        form = FormsBook(request.POST)
        if form.is_valid():
            author = form.cleaned_data["author_name"]
            book = form.cleaned_data["book_name"]
            check_author = form.cleaned_data["author_opt"]
            check_book = form.cleaned_data["book_opt"]

            if check_book == False and check_author == False:
                messages.info(request, 'You have to select a type of search.')
            else:
                if book == "" and check_book == True:
                    messages.info(request, 'Enter the name of a Book')
                if author == "" and check_author == True:
                    messages.info(request, 'Enter the name of an Author')
            
            book_list = services.get_books_by_id()
            return redirect('Results')
    else:
        form = FormsBook()
    context = {'forms': form}
    return render(request, "look4book/index.html", context)

def showResults(request):
    context = {'books': books_results}
    return render(request, "look4book/results.html", context)