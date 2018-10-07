import nltk
from newspaper import Article
from bs4 import BeautifulSoup



def fetch_data(url):
    
    
    url_webpage = url
    article_cnn=Article(url_webpage,language="en")
    article_cnn.download()
    article_cnn.parse()
    #article_cnn.nlp()
    #print("The name of the Article :"+article_cnn.title)
   # print("Body:"+article_cnn.text)
    #print("Summary:"+article_cnn.summary)
    #print("Keywords:")
    #for keyword in article_cnn.keywords:
      #  print(keyword)
    article={
      'heading': article_cnn.title,
      'article_body': article_cnn.text
    }
    return article



#fetch_data('https://www.bbc.com/news/uk-45768848')
#quote_page = 'https://www.cnn.com/2018/10/06/politics/kavanaugh-final-confirmation-vote/index.html'
#page = urllib2.urlopen(quote_page)
#oup=BeautifulSoup(page,'html.parser')

#headline_box = soup.find('h1',attrs={'class':'pg-headline'})
#headline_name = headline_box.text.strip()
#print(headline_name)
#try:
   # import urllib.request as urllib2
#except ImportError:
 #   import urllib2
