from lxml.etree import fromstring
from lxml import html
import os
import datetime

import pandas as pd
import calendar, requests

# set https header parameters
headers = {
	'User-Agent': 'Mozilla/5.0', #required 
	'referer': "https://www.investing.com",
	'host' : 'www.investing.com',
}

class ArticlesData():	

	def __init__(self):
		self.parameters = {'repeated' : True}

		self.articles = {}
		self.xpath_articles = '//section[@id="leftColumn"]/div[@class="mediumTitle1"]/article[@class="articleItem "]/div[@class="textDiv"]/a[@class="title"]'
		self.xpath_article = '//div[@class="arial_14 clear WYSIWYG newsPage"]/p/text()'
		self.article_counter = 0

	#set https header for request
	def setHeaders(self, headers):
		self.headers = headers 

	#desired time period from/to
	def updateStartingEndingDate(self, startingDate, endingDate):
		self.parameters['st_date'] = startingDate	 
		self.parameters['end_date'] = endingDate	 

	#download article titles, urls and dates for desired dates
	def downloadListOfArticles(self, API_url):
		#creates a dictionary included all the articles in the desired time period		
		if DEBUG:
			print("[+] Downloading data from: " + str(API_url))

		page = requests.get(API_url, headers=self.headers)
		tree = html.fromstring(page.content)

		article_titles = list(reversed(tree.xpath(self.xpath_articles + "/text()")))
		article_title_links =  list(reversed(tree.xpath(self.xpath_articles + '//@href')))
		article_dates =  list(reversed(tree.xpath(self.xpath_articles + '/../span[@class="articleDetails"]/span[@class="date"]/text()')))

		for i in range(len(article_titles)):
			article_date = datetime.datetime.strptime(article_dates[i].replace('\xa0-\xa0',''), "%b %d, %Y").date()
			#check if article date is in desired date period
			if self.parameters['st_date'] <= article_date and article_date <= self.parameters['end_date']:
				self.articles[self.article_counter] = {'article_title' : article_titles[i], 'article_title_link' : article_title_links[i], 'article_date' : article_date}
				self.article_counter += 1
			else:
				return False
		return True

	#search also on next pages for articles in the desired time period
	def downloadListOfArticlesRepeatedly(self, API_url):
		#creates a dictionary included all the articles in the desired time period		
		page_counter = 1
		while self.downloadListOfArticles(API_url + "/" + str(page_counter)):
			page_counter += 1		
		if DEBUG:
			print("[+] Scraped " + str(page_counter) + " pages - Articles found: " + str(len(self.articles)))	

	#download all articles from article list dictionary
	def downloadArticleText(self):
		#create directory "/results" if doesn't exists
		if not os.path.exists(str("results")):
			os.makedirs(str("results"))

		#for every article in the dictionary, visit url and scrape text
		for key in sorted(self.articles.keys()):
			if DEBUG:
				print("[+] Downloading article from: " + str('https://www.investing.com/' + self.articles[key]['article_title_link']))
			article = requests.get('https://www.investing.com/' + self.articles[key]['article_title_link'], headers=headers)
			tree = html.fromstring(article.content)
			article_text = ' '.join(tree.xpath(self.xpath_article))
			
			if DEBUG:
				print("[+] Saving data: results/" + str(self.articles[key]['article_date']) + "/" + self.articles[key]['article_title'] + ".txt")
			self.saveArticle("results/" + str(self.articles[key]['article_date']), self.articles[key]['article_title'] + ".txt", article_text)
	
	#save article in .txt format
	def saveArticle(self, directory, filename, text):
		try:
			file = open(directory + "/" + filename, "w")  
			file.write(text) 
			file.close() 
		except FileNotFoundError:
			if not os.path.exists(directory):
				os.makedirs(directory)
				file = open(directory + "/" + filename, "w")  
				file.write(text) 
				file.close() 

	#print article dictionary
	def printListOfArticles(self):
		for key in self.articles:
			print("Title: " + self.articles[key]['article_title'] + "\nURL: " + self.articles[key]['article_title_link'] +  "\nDate: " + str(self.articles[key]['article_date']) + "\n")

if __name__ == "__main__":

	DEBUG = False

	ad = ArticlesData()
	ad.setHeaders(headers)
	ad.updateStartingEndingDate(datetime.date(2017,12, 18), datetime.date(2017,12, 25))
#	ad.downloadListOfArticles("https://www.investing.com/indices/eu-stoxx50-news")
	ad.downloadListOfArticlesRepeatedly("https://www.investing.com/indices/eu-stoxx50-news")
	ad.downloadArticleText()
#	ad.printListOfArticles()

	print("[+] DONE")

