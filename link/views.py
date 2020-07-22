from django.shortcuts import render
from newspaper import Article
import time
# Create your views here.
def link(request):
    return render(request,'link.html')

def withLink(request):
    keyword = request.POST['link']
    article = Article(keyword, language="en")
    article.download()
    while article.download_state == 0:  # ArticleDownloadState.NOT_STARTED is 0
        time.sleep(10)
    article.parse()

    title = article.title
    imglink = article.top_img
    text = article.text
    print(text)
    print('length of text', len(text))
    print(len(article.movies))

    return render(request, 'searchLink.html', {'title': title, 'imglink': imglink, 'text': text})

