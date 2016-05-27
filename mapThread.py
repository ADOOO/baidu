#coding=utf-8
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import requests


urls = ['http://www.wanwei.com.cn']

pool = ThreadPool(4) 

results = pool.map(requests.get, urls)

pool.close() 
pool.join() 

print results[0].text