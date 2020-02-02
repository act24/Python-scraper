#Checking for relevant leads

import pandas as pd
from bs4 import BeautifulSoup
from googlesearch import search
import sys
import html5lib

#read the csv
#infile=input('which file do you want to use? ')
df = pd.read_csv('C:/Users/Admin/Desktop/cleantrial.csv',index_col=False)
print(df.head())
print(df.tail())

list_of_companies = df['Associated Company'].tolist()
list_of_top_results = []
relevance = []
for company in list_of_companies:
        list_of_top_results.append(' '.join(search(company, tld="com", num=10, stop=1, pause=2)))
        print(list_of_top_results[-1])
       
        
import time
import urllib.request
import requests
from urllib.request import urlopen, Request

for url in list_of_top_results:
        #try:
                #change user agent
                agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36\
                (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

                print(url)

                request = Request(url, headers={'User-Agent': agent})  
       

                html = urlopen(request).read().decode()
                soup = BeautifulSoup(html, 'lxml')

                tags = soup.findAll(lambda tag: tag.get('data-id', None) is not None)
                for tag in tags:
                    print(tag['data-id'])
        #except:
                pass
                  

       #time.sleep(2)     



        # Get the title
                title = soup.title
                print(title)

                # Print out the text
                text = soup.get_text()
                #print(text)



                #check for relevant keywords
                if'cart'in text:
                        print('cart')
                        relevance.append('relevant')
                elif'sale'in text:
                        print('sale')
                        relevance.append('relevant')
                elif'gift card'in text:
                        print('gift card')
                        relevance.append('relevant')
                elif'shipping'in text:
                        print('shipping')
                        relevance.append('relevant')
                elif'electronics'in text:
                        print('electronics')
                        relevance.append('relevant')        
                elif'discount'in text:
                        print('discount')
                        relevance.append('relevant')        
                elif 'retail' in text:
                        print('retail')
                        relevance.append('relevant')
                elif'grocery'in text:
                        print('grocery')
                        relevance.append('relevant')
                  
                else:
                        relevance.append('not relevant')
           
       #create new column in outfile for relevance

df['Relevance'] = relevance
#df.insert(12,"relevance",[list_of_top_results],True)
#df.assign(relevan=[list_of_top_results])                        
df.to_csv(r'C:/Users/Admin/Desktop/trial_tagged.csv', index = False)

