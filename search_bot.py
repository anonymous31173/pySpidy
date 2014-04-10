# -*- coding: utf-8
# @mtrpires - http://github.com/mtrpires
from crawler_functions import changePage
from crawler_functions import createCSV
from crawler_functions import downloadHTML
from crawler_functions import fetchLinks
from crawler_functions import findContent
from crawler_functions import findResults
from crawler_functions import numPages
from crawler_functions import setSearchParams
from crawler_functions import storeInfo
from time import sleep
from random import uniform

# Google base search URL
baseURL = "https://www.google.com/search?"

# Initial params
kind = "Revista"
site = "revistaepoca.globo.com"
searchTerm = "Eike Batista"
dateMin = "05/01/2012"
dateMax = "05/31/2013"
perPage = 10
start = 0

# Gets the encoded URL to start the search
params = setSearchParams(site, searchTerm, dateMin, dateMax, perPage, start)
# Downloads the first page from Google
currentHTML = downloadHTML(baseURL, params)
# Saves the number of results. This number is
# used to calculate, roughly, the ammount of pages.
results = findResults(currentHTML)
pages = numPages(results)
# creates the CSV with the toprow
# createCSV()
# empty list where MediaObjects will live.
objectList = []
# The search routine. It goes from page one
# until results/10 + 1 pages. Ex. 213 results will
# render 22 pages. 21 with 10 results, a last one with 3.
# This is only an estimate. Google itself sometimes is
# not 100% sure how many results it gets.
for page in range(pages-start/10):
    # Random sleep
    randomSleep = uniform(2, 5)
    # Populates content list with Google Results
    # from the HTML Soup
    contentList = findContent(currentHTML)
    # Append to the list of objects all relevant information
    # from all the links in that page.
    objectList.append(storeInfo(contentList, kind))
    # Trying not to annoy Google, we try a random
    # short wait.
    print "Catching breath for", randomSleep, "seconds."
    sleep(randomSleep)
    # Go to the next page
    print "Changing page."
    params = changePage(params)
    # Downloads the content of the next page and converts
    # them into a BeautifulSoup object.
    currentHTML = downloadHTML(baseURL, changePage(params))

# Uses the objectList to download all the URLs and
# populate the CSV with relevant information.
#fetchLinks(objectList)

print "The end."
