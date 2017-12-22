# crawler_for_investing.com
Python script - Crawlling indices historical values from investing.com

Create and activate a python3 venv

$ python3 -m venv .venv <br />
$ source .venv/bin/activate<br />

Install requirement.txt

(.venv)$ pip install -r requirements.txt


Files

requirements.txt - required packages <br />
indices.py - contains indices parameters to download <br />
IndiceHistoricalData.py - main function <br />

Choose indice, set Header, set time period and frequency, download data & enjoy! 

Example

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
