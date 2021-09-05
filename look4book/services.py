import os
import requests
import http.client
import json

def get_books():
    url = 'http://openlibrary.org/api/books'
    querystring = {'bibkey': 'ISBN:0201558025','jscmd':'data','format':'json'}
    headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }
    r = requests.get(url, headers=headers, params=querystring )
    # r = requests.request("GET", url, headers=headers, params=querystring)
    
    r.raise_for_status()
    print("statusCode::")
    print(r.status_code)
    books_list = ['ey ey']
    if r.status_code == 200:
        books = r.json()
        print('text::'+r.text)
        print(books)
        
        for i in range(len(books)):
            books_list.append(books['title'][i])
        print(books_list)
    return books_list

def get_books_by_id():
    conn = http.client.HTTPConnection("openlibrary.org")

    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache"
        }

    conn.request("GET", "/api/books?bibkeys=ISBN%3A0201558025%2CLCCN%3A93005405&jscmd=data&format=json", headers=headers)

    res = conn.getresponse()
    data = res.read()
    final_data = data.decode("utf-8")
    books = json.loads(final_data)
    # print(json_obj)

    books_list = []
    for element in books: 
        for value in books[element]:
            if value == 'title':
                books_list.append({'title':books[element][value]})
            # print(books[element]['title'])
     
    print(books_list)
    
    return books_list