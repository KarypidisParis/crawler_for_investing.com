from lxml.etree import fromstring
from lxml import html
import os, datetime, calendar, requests
import pandas as pd

from articles.articlesData import *
from articles.sources import *

# set https header parameters
headers = {
	'User-Agent': 'Mozilla/5.0', #required 
	'referer': "https://www.investing.com",
}

class ArticlesData():	

	def __init__(self, indicatorData):
		self.parameters = {}
		self.articles = {}
		self.indicatorData = indicatorData

		self.article_counter = 0
		self.false_flag = 0			


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
		
		article_titles = tree.xpath(self.indicatorData['xpath_articles'] + self.indicatorData['xpath_articles_title'])
		article_title_links = tree.xpath(self.indicatorData['xpath_articles'] + self.indicatorData['xpath_articles_link'])
		article_dates =  tree.xpath(self.indicatorData['xpath_articles'] + self.indicatorData['xpath_articles_date'])

		try:
			article_titles.remove(" ")
		except ValueError:
			pass
				
		#if ~40 articles are outdated stop the procedure
		for i in range(len(article_titles)):
			#check if 'date' is formet like "Dec 22, 2017" or "11 hours before" or "am" etc
			#if it is set today for date 
			if "hour" in article_dates[i] or "minute" in article_dates[i] or "second" in article_dates[i] or "am" in article_dates[i] or "pm" in article_dates[i]:
				article_dates[i] = datetime.date.today()
				article_date = article_dates[i]
			else:
				if self.indicatorData['name_API'] == 'reuters':
					#find differencies in dates #just a comma
					article_date = datetime.datetime.strptime(article_dates[i].replace('\xa0-\xa0',''), "%b %d %Y").date()					
				elif self.indicatorData['name_API'] == 'investing':	
					article_date = datetime.datetime.strptime(article_dates[i].replace('\xa0-\xa0',''), "%b %d, %Y").date()
#			print(article_date)	

			#check if article date is in desired date period
			if self.parameters['st_date'] <= article_date and article_date <= self.parameters['end_date']:
				article_title = article_titles[i].replace("\n","").replace("\t","")
				if self.filterArticle(article_title):
					self.articles[self.article_counter] = {'article_title' : article_title, 'article_title_link' : article_title_links[i], 'article_date' : article_date}
					self.article_counter += 1
			else:
				self.false_flag += 1
				if self.false_flag >= len(article_titles): #almost 40
					return False		
		return True


	#search also on next pages for articles in the desired time period
	def downloadListOfArticlesRepeatedly(self):
		#creates a dictionary included all the articles in the desired time period		
		page_counter = 1
		while self.downloadListOfArticles(self.indicatorData['url_API'] + str(page_counter)):
			page_counter += 1		
		if DEBUG:
			print("[+] Scraped " + str(page_counter) + " pages - Articles found: " + str(len(self.articles)))	


	#download all articles from article list dictionary
	def downloadArticleText(self):
		#create directory "/results" if doesn't exists
		if not os.path.exists("results"):
			os.makedirs("results")

		#for every article in the dictionary, visit url and scrape text
		for key in sorted(self.articles.keys()):
			#if the artcile is IN the website
			if "http" not in self.articles[key]['article_title_link']:
				if self.indicatorData['name_API'] == 'reuters':
					article_url = 'https://www.reuters.com' + self.articles[key]['article_title_link']
				elif self.indicatorData['name_API'] == 'investing':
					article_url = 'https://www.investing.com' + self.articles[key]['article_title_link']
			#or is from another source
			else:
				article_url = self.articles[key]['article_title_link']
			if DEBUG:
				print("[+] Downloading article from: " + article_url)
			
			article = requests.get(article_url, headers=headers)
			tree = html.fromstring(article.content)
			#check for every possible source (file: articles/sources.py)
			for source in sources:
				article_text = ' '.join(tree.xpath(sources[source]['xpath_article']))
				if article_text is not "":			
					if DEBUG:
						print("[+] Source: " + str(source))
						print("[+] Saving data: results/" + str(self.articles[key]['article_date']) + "/" + self.articles[key]['article_title'] + ".txt")
					self.saveArticle("results/" + str(self.articles[key]['article_date']), self.articles[key]['article_title'].replace("/"," ") + ".txt", article_text)
					
	
	#save article in .txt format
	def saveArticle(self, directory, filename, text):
		try:
			file = open(directory + "/" + filename, "w")  
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


	#filter article title for certain words
	def filterArticle(self, title):
		for title_word in title.split(" "):
			if title_word in self.indicatorData['listOfWords']:
				return True
		return False



if __name__ == "__main__":

	DEBUG = True
	
	indicator = eurostoxx_reuters

	ad = ArticlesData(indicator)
	ad.setHeaders(headers)
	ad.updateStartingEndingDate(datetime.date(2017,12, 20), datetime.date(2017,12, 27))
	ad.downloadListOfArticlesRepeatedly()
#	ad.printListOfArticles()

	ad.downloadArticleText()
	print("[+] DONE")

