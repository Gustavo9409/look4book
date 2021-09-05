from django.shortcuts import render
from . import services

# This function initialize home page
# request: The request object used to generate this response.
# Returns the render of home template

def initHome(request):
    book_list = services.get_books2()
    context = {'books': []}
    return render(request, "look4book/index.html", context)