from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordcount = fulltext.split()

    word1 = {}
    for word in wordcount:
        if word in word1:
            word1[word] += 1
        else:
            word1[word] = 1

    return render(request, 'count.html',{'fulltext': fulltext, 'wordcount': len(wordcount), 'word1': word1.items()})
