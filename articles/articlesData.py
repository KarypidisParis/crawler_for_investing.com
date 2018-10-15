'''
INVESTING.COM
*	sometimes 'articleItem' is 'articleItem ' this patch corrects this -> node()	
*	sometimes '/span[@class='articleDetails']' is '/div[@class='articleDetails'] ' this patch corrects this -> node()
REUTERS.COM
*	sometimes 'news-headline-list' is 'news-headline-list  ' this patch corrects this -> node()	
*	sometimes 'story' is 'story ' this patch corrects this -> node()	
'''

#https://www.investing.com/news/commodities-news/
oil = {
	'name_API' : 'investing',
	'url_API' : 'https://www.investing.com/news/commodities-news/',
	'xpath_articles' : '//section[@id="leftColumn"]/div[@class="largeTitle"]/node()[not(@class="articleItem sponsoredArticle ")]/div[@class="textDiv"]',
	'xpath_articles_title' : '/a[@class="title"]/text()',
	'xpath_articles_link' : '/a[@class="title"]//@href',
	'xpath_articles_date' : '/node()/span[@class="date"]/text()',
	'listOfWords' : ['Oil', 'Brent', 'Crude', 'OPEC', 'WTI', 'OIL', 'BRENT', 'CRUDE']
}

#https://www.investing.com/currencies/eur-usd-news/
eurodollar = {
	'name_API' : 'investing',
	'url_API' : 'https://www.investing.com/currencies/eur-usd-news/',
	'xpath_articles' : '//section[@id="leftColumn"]/div[@class="mediumTitle1"]/node()[not(@class="articleItem sponsoredArticle ")]/div[@class="textDiv"]',
	'xpath_articles_title' : '/a[@class="title"]/text()',
	'xpath_articles_link' : '/a[@class="title"]//@href',
	'xpath_articles_date' : '/node()/span[@class="date"]/text()',
	'listOfWords' : ['EUR/USD', 'EURO', 'EUR', 'Eur/Usd', 'eur/usd', 'euro', 'eur']
}

#https://www.investing.com/news/stock-market-news/
eurostoxx = {
	'name_API' : 'investing',
	'url_API' : 'https://www.investing.com/news/stock-market-news/',
	'xpath_articles' : '//section[@id="leftColumn"]/div[@class="largeTitle"]/node()[not(@class="articleItem sponsoredArticle ")]/div[@class="textDiv"]',
	'xpath_articles_title' : '/a[@class="title"]/text()',
	'xpath_articles_link' : '/a[@class="title"]//@href',
	'xpath_articles_date' : '/node()/span[@class="date"]/text()',
	'listOfWords' : ['Europe', 'European', 'FTSE', 'Euro Zone', 'Eurozone']
}

#https://www.investing.com/indices/eu-stoxx50-news/
eurostoxx_v2 = {
	'name_API' : 'investing',
	'url_API' : 'https://www.investing.com/indices/eu-stoxx50-news/',
	'xpath_articles' : '//section[@id="leftColumn"]/div[@class="mediumTitle1"]/node()[not(@class="articleItem sponsoredArticle ")]/div[@class="textDiv"]',
	'xpath_articles_title' : '/a[@class="title"]/text()',
	'xpath_articles_link' : '/a[@class="title"]//@href',
	'xpath_articles_date' : '/node()/span[@class="date"]/text()',
	'listOfWords' : ['Europe', 'European', 'FTSE', 'Euro Zone', 'Eurozone']
}

#https://www.reuters.com/news/archive/europe-stocks?view=page&page=
eurostoxx_reuters = {
	'name_API' : 'reuters',
	'url_API' : 'https://www.reuters.com/news/archive/europe-stocks?view=page&page=',
	'xpath_articles' : '//div[@class="column1 col col-10"]/section[@class="module  "]/section[@class="module-content"]/node()/node()/div[@class="story-content"]',
	'xpath_articles_title' : '/a/h3[@class="story-title"]/text()',
	'xpath_articles_link' : '/a//@href',
	'xpath_articles_date' : '/time[@class="article-time"]/span[@class="timestamp"]/text()',
	'listOfWords' : ['Europe', 'European', 'FTSE', 'Euro Zone', 'Eurozone']
}

