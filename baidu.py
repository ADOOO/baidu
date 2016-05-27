#coding=utf-8

import time 
import threading 
import Queue
import requests
import sys
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
    'Referer' : 'http://www.google.com',
    'Cookie': 'whoami=wyscan_dirfuzz',
    }
threads_count = 10
f = open('out.txt','w')
f.close()
#search_url = 'https://www.baidu.com/s?wd=[keyword]&pn=0&oq=test&tn=baiduhome_pg&ie=utf-8&usm=1&rsv_idx=2&rsv_pq=e4898687000090e5&rsv_t=7498TKRyJmN3O29jzKMSPeCjSIryB6PKiuhLvYDOTBJGsqwDCFdZF3oxzqSa1Xjbofrt'
search_url_start = 'https://www.baidu.com/s?wd='
search_url_end = '&tn=baiduhome_pg&ie=utf-8&usm=1&rsv_idx=2&rsv_pq=e4898687000090e5&rsv_t=7498TKRyJmN3O29jzKMSPeCjSIryB6PKiuhLvYDOTBJGsqwDCFdZF3oxzqSa1Xjbofrt'
urllist = []

class BaiduScan(threading.Thread): 
    def __init__(self, queue): 
        threading.Thread.__init__(self)
        self._queue = queue 

    def run(self):
        while not self._queue.empty():
            try:
                msg = self._queue.get_nowait() 
                r = requests.get(url=msg,headers=headers)
                soup = BeautifulSoup(r.text,'html.parser')
                for i in soup.find_all('h3'):
                    h3 = str(i)

                    baidu_soup = BeautifulSoup(h3,'html.parser')
                    baidu_url = baidu_soup.find('a').get('href')
                    #print baidu_url
                    true_url = requests.get(url=baidu_url, headers=headers)
                    url_t = true_url.url
                    if url_t in urllist:
                        pass
                    else:
                        urllist.append(true_url.url)
                        print true_url.url
                        #true_url = re.findall('"(.*?)"',true_url.text)[0]
                        
                        if 'baidu.com' in true_url:
                            pass
                        else:
                            #print true_url
                            f = open('out.txt','a+')
                            f.write(true_url.url)
                            f.write('\n')
                            f.close()

            except Exception,e:
                #print e
                pass

def search(keyword):
#def search():
    queue = Queue.Queue()
    for i in range(0,800,10):
        queue.put(search_url_start+keyword+'&pn='+str(i)+search_url_end)

    threads = []
    for i in xrange(threads_count):
        threads.append(BaiduScan(queue))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print 'Done!!!!!!!!!!'

if __name__ == '__main__':

    if len(sys.argv) == 2:
        search(sys.argv[1])
        sys.exit(0)
    else:
        print ("usage: %s keyword" % sys.argv[0])
        sys.exit(-1)

    #search()