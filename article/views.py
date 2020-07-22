from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from newspaper import Article
from feed.views import available_link,website
import time
# Create your views here.
special_websites=['amazon','flipkart','youtube']
def article1(request):

    print (len(available_link))
    #print (len(links))
    #print(links)
    #urls=list(url)
    url1= available_link[0]
    article = Article(url1, language="en")
    article.download()
    while article.download_state == 0:  # ArticleDownloadState.NOT_STARTED is 0
        time.sleep(10)
    article.parse()

    title=article.title
    imglink =article.top_img
    text=article.text
    print(text)
    print('length of text',len(text))
    print(len(article.movies))


    if len(text)<=250 or website[0] in special_websites:
        return redirect(available_link[0])

    else:
        return render(request, 'article.html',{'title': title, 'imglink': imglink, 'text': text, 'link': available_link[0]})


def article2(request):
    #print(len(available_link))
    #print(links)
    # urls=list(url)
    url2 = available_link[1]
    article = Article(url2, language="en")
    article.download()
    while article.download_state == 0:  # ArticleDownloadState.NOT_STARTED is 0
        time.sleep(10)
    article.parse()

    title = article.title
    imglink = article.top_img
    text = article.text
    if len(text) <= 250 or website[1] in special_websites:
        return redirect(available_link[1])
    else:
        return render(request, 'article.html', {'title': title, 'imglink': imglink, 'text': text, 'link': available_link[1]})


def article3(request):
    #print(len(links))
    # print(links)
    # urls=list(url)
    url3 = available_link[2]
    article = Article(url3, language="en")
    article.download()
    while article.download_state == 0:  # ArticleDownloadState.NOT_STARTED is 0
        time.sleep(10)
    article.parse()

    title = article.title
    imglink = article.top_img
    text = article.text
    if len(text) < 250 or website[2] in special_websites:
        return redirect(available_link[2])
    else:
        return render(request, 'article.html', {'title': title, 'imglink': imglink, 'text': text, 'link': available_link[2]})

def article4(request):
    #print(len(links))
    # print(links)
    # urls=list(url)
    url4 = available_link[3]
    article = Article(url4, language="en")
    article.download()
    while article.download_state == 0:  # ArticleDownloadState.NOT_STARTED is 0
        time.sleep(10)
    article.parse()

    title = article.title
    imglink = article.top_img
    text = article.text
    if len(text) <= 250 or website[3] in special_websites:
        return redirect(available_link[3])
    else:
        return render(request, 'article.html', {'title': title, 'imglink': imglink, 'text': text, 'link': available_link[3]})

def article5(request):
   # print(len(links))
    # print(links)
    # urls=list(url)
    url5 = available_link[4]
    article = Article(url5, language="en")
    article.download()
    while article.download_state == 0:  # ArticleDownloadState.NOT_STARTED is 0
        time.sleep(10)
    article.parse()

    title = article.title
    imglink = article.top_img
    text = article.text
    print(len(text))


    if len(text) <= 250 or website[4] in special_websites:
        return redirect(available_link[4])
    else:
        return render(request, 'article.html', {'title': title, 'imglink': imglink, 'text': text, 'link': available_link[4]})

def article6(request):
    #print(len(links))
    # print(links)
    # urls=list(url)
    url6 = available_link[5]
    article = Article(url6, language="en")
    article.download()
    while article.download_state == 0:  # ArticleDownloadState.NOT_STARTED is 0
        time.sleep(10)
    article.parse()

    title = article.title
    imglink = article.top_img
    text = article.text
    if len(text) <= 250 or website[5] in special_websites:
        return redirect(available_link[5])
    else:
        return render(request, 'article.html', {'title': title, 'imglink': imglink, 'text': text, 'link': available_link[5]})

def article7(request):
    #print(len(links))
    # print(links)
    # urls=list(url)
    url7 = available_link[6]
    article = Article(url7, language="en")
    article.download()
    while article.download_state == 0:  # ArticleDownloadState.NOT_STARTED is 0
        time.sleep(10)
    article.parse()

    title = article.title
    imglink = article.top_img
    text = article.text
    if len(text)<=250 or website[6] in special_websites:
        return redirect(available_link[6])
    else:
        return render(request, 'article.html', {'title': title, 'imglink': imglink, 'text': text, 'link': available_link[6]})

def article8(request):
    #print(len(links))
    # print(links)
    # urls=list(url)
    url8 = available_link[7]
    article = Article(url8, language="en")
    article.download()
    while article.download_state == 0:  # ArticleDownloadState.NOT_STARTED is 0
        time.sleep(10)
    article.parse()

    title = article.title
    imglink = article.top_img
    text = article.text
    if len(text)<=250 or website[7] in special_websites:
        return redirect(available_link[7])
    else:
        return render(request, 'article.html', {'title': title, 'imglink': imglink, 'text': text, 'link': available_link[7]})

def article9(request):
    #print(len(links))
    # print(links)
    # urls=list(url)
    url9= available_link[8]
    article = Article(url9, language="en")
    article.download()
    while article.download_state == 0:  # ArticleDownloadState.NOT_STARTED is 0
        time.sleep(10)
    article.parse()

    title = article.title
    imglink = article.top_img
    text = article.text
    if len(text)<=250 or website[8] in special_websites:
        return redirect(available_link[8])
    else:
        return render(request, 'article.html', {'title': title, 'imglink': imglink, 'text': text, 'link': available_link[8]})

