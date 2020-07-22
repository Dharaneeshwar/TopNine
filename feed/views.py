from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from newspaper import Article
import time
from googlesearch import search
from .models import feeditem
import re

# Create your views here.
def about(request):
    return render(request,'about.html')
website=[]
def home(request):
    return render(request, 'home.html')
links=[]
available_link=[]
def searchit(request):
    keyword = request.GET['key']

    imglinks=[]
    titles=[]

    links.clear()
    available_link.clear()
    for j in search(keyword, tld="co.in", num=20, stop=20, pause=2):
        links.append(j)
    #print(links)

    while len(links) <= 9:
        keyword=keyword+' news'
        for j in search(keyword, tld="co.in", num=40, stop=40, pause=4):
            links.append(j)

   # print(links)
    print('links :',len(links))

    item1 = feeditem()
    item2 = feeditem()
    item3 = feeditem()
    item4 = feeditem()
    item5 = feeditem()
    item6 = feeditem()
    item7 = feeditem()
    item8 = feeditem()
    item9 = feeditem()

    print('\n')
    print('available_link :',len(available_link))
    #print(available_link)

    for link in links:
        article = Article(link, language="en")
        try:

            # To download the article

            article.download()
            while article.download_state == 0:  # ArticleDownloadState.NOT_STARTED is 0
                time.sleep(5)
            article.parse()
            #top_img = article.top_image
                # To extract title


                # to extract image

            if article.title!= None :
                p_y=re.compile('https://www.youtube.com/')
                m_y=p_y.match(link)
                p_f = re.compile("https://www.flipkart.com/")
                m_f = p_f.match(link)
                if m_y:
                    titles.append(article.title)
                    imglinks.append(article.top_image)
                    available_link.append(link)
                    website.append('youtube')

                if m_f:
                    titles.append(article.title)
                    available_link.append(link)
                    imglinks.append('')
                    website.append('flipkart')


                if article.title =="Robot Check":
                    titles.append('Buy on Amazon')
                    website.append('amazon')
                    imglinks.append('')
                    available_link.append(link)


                if article.title !="Robot Check" and m_f== None and m_y == None:

                    titles.append(article.title)
                    imglinks.append(article.top_image)
                    available_link.append(link)
                    website.append('general')
        except:
            continue


    print('available links :',len(available_link))
    print(available_link)
    print('titles :', len(titles))
    print(titles)
    print('imagelinks :',len(imglinks))
    print(imglinks)
    print(website)

    item1.title =titles[0]
    item1.imglink = imglinks[0]
    item1.pglink= available_link[0]
    item1.website=website[0]

    item2.title = titles[1]
    item2.imglink = imglinks[1]
    item2.pglink = available_link[1]
    item2.website = website[1]

    item3.title = titles[2]
    item3.imglink = imglinks[2]
    item3.pglink = available_link[2]
    item3.website = website[2]

    item4.title = titles[3]
    item4.imglink = imglinks[3]
    item4.pglink = available_link[3]
    item4.website = website[3]

    item5.title = titles[4]
    item5.imglink = imglinks[4]
    item5.pglink = available_link[4]
    item5.website = website[4]

    item6.title = titles[5]
    item6.imglink = imglinks[5]
    item6.pglink = available_link[5]
    item6.website = website[5]

    item7.title = titles[6]
    item7.imglink = imglinks[6]
    item7.pglink = available_link[6]
    item7.website = website[6]

    item8.title = titles[7]
    item8.imglink = imglinks[7]
    item8.pglink = available_link[7]
    item8.website = website[7]

    item9.title = titles[8]
    item9.imglink = imglinks[8]
    item9.pglink = available_link[8]
    item9.website = website[8]

    return render(request, 'feed.html',{'item1':item1,'item2':item2,'item3':item3,'item4':item4,'item5':item5,'item6':item6,'item7':item7,'item8':item8,'item9':item9})

