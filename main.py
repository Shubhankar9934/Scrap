#! D:\Web_Scrapping\venv\Scripts\python.exe
# import requests
# import csv
# import json
# r = requests.get("https://quotes.toscrape.com/")
# print(r.status_code)

# html = r.text
# with open('quotes.txt','w',encoding='utf-8') as f:
#     for line in html.split("\n"):
#         if '<span class="text" itemprop="text">' in line: 
#             line = line.replace('<span class="text" itemprop="text">“' , "").replace('”</span>',"")
#             line = line.strip()
#             f.write(line)
#             f.write('\n')

# html = r.text
# with open('author.txt', 'w' ,encoding='utf-8') as f:
#     for line in  html.split('\n'):
#         if '<span>by <small class="author" itemprop="author">' in line:
#             line = line.replace('<span>by <small class="author" itemprop="author">' , "").replace('</small>' , "")
#             line = line.strip()
#             f.write(line)
#             f.write('\n')



#Pagination
# with open('quotes_final.txt','w' , encoding='utf-8') as f:
#     for i in range(1,11):
#         #print(f'https://quotes.toscrape.com/{i}/')
#         url = f"https://quotes.toscrape.com/page/{i}/"
#         r = requests.get(url)
#         html = r.text
#         for line in html.split('\n'):
#             if '<span class="text" itemprop="text">' in line:
#                 line = line.replace('<span class="text" itemprop="text">“','').replace('”</span>', '')
#                 line = line.strip()
#                 f.write(line)
#                 f.write('\n')

# I want To extract quotes and author names from the website and save them in a CSV file named "quotes_author.csv" of 10 pages

# with open('quotes_author.csv', 'w',encoding='utf-8') as f:
#     for i in range(1,11):
#         url = f'https://quotes.toscrape.com/page/{i}/'
#         r = requests.get(url)
#         html = r.text

#         for line in html.split('\n'):
#             if '<span class="text" itemprop="text">' in line:
#                 quote = line.replace('<span class="text" itemprop="text">“','').replace('”</span>','')
#                 quote = quote.strip()
#                 #quotes.append(quote)
#             if '<span>by <small class="author" itemprop="author">' in line:
#                 author = line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
#                 author = author.strip()
#                 #authors.append(author)
#                 f.write(author + ',' + quote)
#                 f.write('\n')


#espncrickinfo

# url = 'http://www.espncricinfo.com/ci/content/story/data/index.json?;type=7;page=1'

# r = requests.get(url)
# data = json.loads(r.text)
# #print(data)

# #print(type(data))
# with open('data.txt', 'w') as f:
#     for news in data:
#         f.write(news['author'] +' : ' + news['summary'])
#         f.write('\n')
#         f.write('--------------------------------')
#         f.write('\n')


# Pagination for the story espncrickinfo
# with open('data_final.txt', 'w') as f:
#     for i in range(1,11):
#         url = f'http://www.espncricinfo.com/ci/content/story/data/index.json?;type=7;page={i}'
#         r = requests.get(url)
#         #print(f'page - {i}' , ' : ' ,r.status_code)
#         data = json.loads(r.text)
#         for news in data:
#             f.write(news['author'] + ' : ' + news['summary'])
#             f.write('\n')
#             f.write('--------------------------------')
#             f.write('\n')

# superstats scrap from espncrickinfo

# url = 'https://hs-consumer-api.espncricinfo.com/v1/pages/matches/current?lang=en&latest=true'

# r = requests.get(url)
# #print(r.status_code)
# with open('stats.txt', 'w') as f:
#     data = json.loads(r.text)
#     data = data['matches']
    
#     for news in data:
#         news = news['slug']
#         news = news.strip()
#         f.write(news)
#         f.write('\n')

    
