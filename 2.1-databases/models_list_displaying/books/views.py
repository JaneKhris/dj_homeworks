from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {
        'books': [],
    }
    books = Book.objects.all()
    for book in books:
        context['books'].append(book)
    return render(request, template, context)

def pagi_date(request,date):
    pub_date = datetime.strptime(date, '%Y-%m-%d').date()
    template = 'books/books_pagi.html'
    book_list = Book.objects.order_by('pub_date')
    book_dict = {}
    dict_date_page = {}
    pub_date_list = []
    CONTENT = []
    for book in book_list:
        book_dict.setdefault(book.pub_date, [])
        book_dict[book.pub_date].append(book)
    p_page = 1
    for p_date, books in book_dict.items():
        dict_date_page.setdefault(p_date, p_page)
        CONTENT.append({p_date:books})
        p_page += 1
        pub_date_list.append(datetime.strftime(p_date, '%Y-%m-%d'))
    paginator = Paginator(CONTENT,1)
    page_number = dict_date_page.get(pub_date)
    page = paginator.get_page(page_number)
    books_page = (list(list(page)[0].values()))[0]
    if page_number <= len(pub_date_list)-1:
        date_next = pub_date_list[page_number]
    else:
        date_next = None
    context = {
        'page': page,
        'books': books_page,
        'date_previous': pub_date_list[page_number-2],
        'date_next': date_next,

    }
    return render(request, template, context)