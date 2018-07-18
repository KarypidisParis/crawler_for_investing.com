sources = {
	'investing' : {'xpath_article' : '//div[@class="arial_14 clear WYSIWYG newsPage"]/p/text()'},
	'reuters' : {'xpath_article' : '//div[@class="TwoColumnLayout_column_1uZPg TwoColumnLayout_left_qEP9d"]/div[@class="StandardArticleBody_container_17wb1"]/div[@class="StandardArticleBody_body_1gnLA"]//text()'},
	'fxempire' : {'xpath_article' : '//article[@class="Post__PostArticle-a0rnwa-0 eVaNwM"]/div[@class="Body-s52xhdz-0 fzCZGI"]//text()'},	
	'talkmarkets' : {'xpath_article' : '//div[@id="content"]/div[@class="card"]/div[@class="tm-article_card-block"]/div[@id="blog-content"]//text()'},
	'fxstreet' : {'xpath_article' : '//article[@class="fxs_article"]/div[@class="fxs_row sticky-holder"]/div[@class="fxs_flex_col"]/div[@class="fxs_article_body"]//text()'},
	'stocknewsjournal' : {'xpath_article' : '//div[@class="td-pb-row"]/div[@class="td-pb-span8 td-main-content"]/div[@class="td-ss-main-content"]/node()/div[@class="td-post-content"]/p//text()'},
	'briefing' : {'xpath_article' : '//div[@id="content"]/div[@class="story-wrapper"]/div[@class="summary-wrapper"]/div[2]//text()'},	
}
