#coding=utf-8
from bs4 import BeautifulSoup

html = '''
<h3 class="t"><a 
	        data-click="{
			'F':'778717EA',
			'F1':'9D73F164',
			'F2':'4CA6DE6B',
			'F3':'54E5243F',
			'T':'1451442179',
						'y':'EFEED6C0'
			 
									}"
        href = "http://www.baidu.com/link?url=dP3qw51zbrVB6e7F5lplEsh6oc5FCvTYlykVvdiOmgseo-dfhxhr_Blb404MELEcQmdt8iCqrc5Xry0Q3XtUwK"

		            target="_blank"
        		
		>清迈,绝对实用的良心攻略--清迈游记--蚂蜂窝</a></h3>
		'''

soup = BeautifulSoup(html,'html.parser')

print soup.find('a').get('href')