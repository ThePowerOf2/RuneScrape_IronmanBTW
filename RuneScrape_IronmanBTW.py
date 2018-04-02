# Imports
import bs4 as bs # Used handle the HTML code.
import urllib.request # Used to fetch the HTML Code.

# Group level limits + number of pages to scrape + what skill to scrape.
noPages = 8

# Declaring an array for each group.
names=[]

# Counters.
x,y = 0

# Creating/Overwriting .txt file to save names into.
namesFile = open("NeepisBae.txt","w")

# For loop from 1 to amount of (pages+1).
for memes in range(1,noPages+1):

	# The URL of the website to be scraped.
	URL = "http://www.runeclan.com/clan/reclusion/hiscores/%s" % (memes)

	# Fetching the HTML code from the URL.
	sauce = urllib.request.urlopen(URL).read()

	# Formating the HTML code with BeautifulSoup.
	soup = bs.BeautifulSoup(sauce, 'lxml')

	# Scraping Down to the information we want.
	div = soup.find('td',class_='clan_right')
	table = div.find('table',class_='regular')
	table_rows = table.find_all('tr')

	# Place all names into an array from teh table we've scraped.
	for tr in table_rows:
		if x%2 == 0:
			td = tr.find_all('td')
			row = [i.text for i in td]
			names.append(row[1])
		x=x+1

	# Print out when a page has been completed.
	print('Page %d Complete.' % (memes))

# For each name sorted in alphebetical order.
for name in sorted(names, key=lambda s: s.lower()):

	# Printing Progress along with name being worked on.
	print("%i / %i %s" % (y,names.length,name))

	# Scraping out a blank or an error report based on the name given.
	URL = "http://services.runescape.com/m=hiscore_ironman/ranking?user=%s" % (name.lower())
	sauce = urllib.request.urlopen(URL).read()
	soup = bs.BeautifulSoup(sauce, 'lxml')
	div = soup.find('div',class_='tempHSUserSearchError')

	# Placing names that did not get an Error(Therefore Ironmen) into a text file.
	if div == None:
		namesFile.write(name)
		namesFile.write("\n")

# Memes
print('Finished!')