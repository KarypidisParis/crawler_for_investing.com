# crawler_for_investing.com
Python script - Crawlling indices historical values and Articles from investing.com

Create and activate a python3 venv

$ python3 -m venv .venv <br />
$ source .venv/bin/activate<br />

Install requirement.txt

(.venv)$ pip install -r requirements.txt


Files

requirements.txt - required packages <br />
indices.py - contains indices parameters to download <br />
IndiceHistoricalData.py - main function <br />
Articles.py - main function <br />

Download Indices Historical Values

Choose indice, set Header, set time period and frequency, download data & enjoy! 

Example - See IndiceHistoricalData.py

	#first set Headers and FormData	
	ihd = IndiceHistoricalData('https://www.investing.com/instruments/HistoricalDataAjax')
	ihd.setHeaders(headers)
	ihd.setFormData(NGF8)
	
	#second set Variables
	ihd.updateFrequency('Monthly')
	ihd.updateStartingEndingDate('1/1/2010', '12/20/2017')
	ihd.setSortOreder('ASC')
	ihd.downloadData()
	ihd.printData()
	ihd.saveDataCSV()

Download Articles

Set Header, set time period, download data, save as .txt & enjoy! 

Example - See Articles.py

	ad = ArticlesData()
	ad.setHeaders(headers)
	ad.updateStartingEndingDate(datetime.date(2017,12, 18), datetime.date(2017,12, 25))
#	ad.downloadListOfArticles("https://www.investing.com/indices/eu-stoxx50-news")
	ad.downloadListOfArticlesRepeatedly("https://www.investing.com/indices/eu-stoxx50-news")
	ad.downloadArticleText()
#	ad.printListOfArticles()
