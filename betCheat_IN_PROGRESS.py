import bs4, requests, re, random, time
from selenium import webdriver

#variables
lostPerHundred = 10
no_popup = True
minBetAll = 1.6

#new betting sites:
newBettingSites = []

class NewBettingSite():
	def __init__(self,minBet,maxDeposit,link):
		self.minBet = minBet
		self.maxDeposit = maxDeposit
		self.link = link
		newBettingSites.append(self)
	def GetLink(self):
		if self.link == "https://sports.bwin.dk/da/sports":
			headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
			self.res = requests.get("https://sports.bwin.dk/da/sports",headers=headers)
		else:
			self.res = requests.get(self.link)
		self.res.raise_for_status()
	def MakeSoup(self):
		self.soup = bs4.BeautifulSoup(self.res.text,"html.parser")

betfair = NewBettingSite(1.95,1000,"https://www.betfair.com/sport/") 
comeon = NewBettingSite(1.8,500,"https://www.comeon.com/da/sportsbook")
bwin = NewBettingSite(1.7,500,"https://sports.bwin.dk/da/sports")

for bettingSite in newBettingSites:
	bettingSite.GetLink()
	bettingSite.MakeSoup()




#old betting sites:

oldBettingSites = []

class OldBettingSite():
	def __init__(self,link):
		self.link = link
		oldBettingSites.append(self)
	def GetLink(self):
		self.res = requests.get(self.link)
		self.res.raise_for_status()
	def MakeSoup(self):
		self.soup = bs4.BeautifulSoup(self.res.text,"html.parser")

danskeSpil = OldBettingSite("https://danskespil.dk/oddset/")
bet365 = OldBettingSite("https://www.bet365.dk/?forcelp=1&affiliate=365_726725#/HO/")
unibet = OldBettingSite("https://www.unibet.dk/")
triple8 = OldBettingSite("https://www.888sport.dk/?deeplink=opennrs&promo=500back#/home")

for bettingSite in oldBettingSites:
	bettingSite.GetLink()
	bettingSite.MakeSoup()

#def FindSameSport(oldSites,newSites,sport):
#	results = []
#	pattern = re.compile(sport)
#	for sites in oldSites:
#		result = sites.soup.findAll("td", text = pattern, attrs={'class' : 'pos'})
#		results.append(result)
#	print(results)


	#skal returne 2 lister - old + new hvor de har "trykket" på den rigtige sport
browser = webdriver.Chrome()


def CheckForPopUp():
	close_button = browser.find_elements_by_css_selector("#messages-with-overlay > div > vn-content-message > div > span")
	if len(close_button) > 0:
		global no_popup
		no_popup = False

def AcceptPopUp():
	accept_button = browser.find_element_by_css_selector("#messages-with-overlay > div > vn-content-message > div > span")
	accept_button.click()

def FindSport(sport, startSite):
	if startSite == bwin:
		if sport == "Tennis":
			browser.get(startSite.link + "/tennis-5")
		elif sport == "Fodbold":
			browser.get(startSite.link + "/fodbold-4")
	else:
		browser.get(startSite.link)
	while no_popup:
		CheckForPopUp()
		time.sleep(0.1)
	else:
		AcceptPopUp()
	sport_elem = browser.find_element_by_partial_link_text(sport)
	sport_elem.click()

def FindNumberOfLiveMatches(list_of_all_parents):
	numberOfLiveMatches = 0
	for parent in list_of_all_parents:
		if parent.find_elements_by_class_name("live-icon"):
			numberOfLiveMatches += 1
	return numberOfLiveMatches

def FindParentsNoLive():
	#tournament = browser.find_element_by_css_selector("#main-content > ms-main > ms-column > div.column-container > ms-competition-navigation > ms-competition-tree > ms-item-tree:nth-child(1) > ms-item-tree > ms-item.leaf-item.list-item.ng-star-inserted.active")
	#tournament.click()
	list_of_all_parents = browser.find_elements_by_tag_name("ms-event") #giver det samme som grid_event
		#kan være en af disse for class:
			#grid-event
		 	#ms-active-highlight 
		 	#ng-star-inserted
	#print(list_of_all_parents[0].text)
	numberOfLiveMatches = FindNumberOfLiveMatches(list_of_all_parents)
	list_of_all_parents_not_live = list_of_all_parents[numberOfLiveMatches:-1:1]
	return list_of_all_parents_not_live

def FindCorrectBets(parents):
	indexOfProperBets = []
	ratioList = []
	for parent in parents:
		betRatio = parent.find_elements_by_class_name("grid-option-group")
		#for some reason we don't get the first of the non-live
		#print(betRatio[0].text)
		ratioListInProgress = betRatio[0].text.split("\n")
		try:
			float(ratioListInProgress[0])
			ratioList.append(ratioListInProgress)
		except:
			pass
	currentIndex = 0
	for betPair in ratioList:
		if float(betPair[0]) > minBetAll and float(betPair[1]) > minBetAll:
			indexOfProperBets.append(betPair.index)
		currentIndex += 1
	print(indexOfProperBets)

		




FindSport("Tennis",bwin)
parentsNoLive = FindParentsNoLive()
FindCorrectBets(parentsNoLive)
#prøv med selenium
	#return liste med all parents - skal kun have dem hvor begge odds er over 1,6
	#skal finde de samme navne for mindst en oldsite og newsite (helst flere)
	#kør function som tjekker om det er profitabel baseret på lostPerHundred
		#denne skal køre først på en af siderne, derefter skal der sammenlignes med bettingsitesne

	#hvis det er for svært kan vi bare gør det med en newsite, sammenlignet med de oldsites, og så gøre det en gang for hver