import sys,time, random, bs4, requests, pyautogui, pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.Chrome()
#action = ActionChains(browser) 
def GetToGmailSignUp():
	browser.get("https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp")

def GetToProtonMailSignUp():
	browser.get("https://mail.protonmail.com/create/new?language=da")

def CheckLoading(classOfElement):
	loading = True
	while loading == True:
		time.sleep(0.1)
		try:
			browser.find_element_by_class_name(classOfElement)
		except:
			loading = False
	return



def RandomNameGenerator():
	firstNames = ["William", "Alfred", "Oscar", "Noah", "Karl", "Lucas", "Oliver", "Arthur", "August",  "Malthe", "Valdemar", "Emil", "Victor", "Aksel", "Elias", "Magnus", "Viggo", "Anton", "Felix", "Frederik", "Nohr", "Alexander", "Theo", "Elliot", "Otto", "Lauge", "Hugo", "Liam", "Villads", "Theodor", "Loui", "Milas", "Anker", "Albert",  "Johan", "Storm", "Adam", "Mikkel", "Christian", "Matheo", "Konrad", "Pelle", "Villum", "Benjamin", "Erik", "Asgar", "Mads", "Walter", "Marius", "Mathias"]
	lastNames = ["Andersen", "Andersson", "Andreasen", "Andreassen", "Andresen", "Asmussen", "Bach", "Bak", "Bang", "Bech", "Beck", "Bendtsen", "Berg", "Bertelsen", "Berthelsen", "Bisgaard", "Bjerre", "Bjerregaard", "Bonde", "Brandt", "Brodersen", "Bruun", "Buch", "Bundgaard", "Carlsen", "Carstensen", "Christensen", "Christiansen", "Christoffersen", "Clausen", "Dahl", "Hansen", "Dalgaard", "Larsen", "Dalsgaard", "Dam", "Jensen"]
	fullName = random.choice(firstNames) + "_" + random.choice(lastNames)
	return fullName

def GetFirstName(fullName):
	fullNameList = fullName.split("_")
	firstName = fullNameList[0]
	return firstName

def GetLastName(fullName):
	fullNameList = fullName.split("_")
	lastName = fullNameList[1]
	return lastName

def RandomUserNameGenerator(fullName):
	extraForUserName = ""
	for digitInName in range(5):
		extraForUserName += str(random.randint(0,9))
	userName = fullName + extraForUserName 
	print(userName)
	return userName


def RandomPasswordGenerator(passwordLength):
	capitalLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	nonCapitalLetters = "abcdefghjiklmnopqrstuvwxyz"
	newPassword = ""
	whatToInsertIndex = 0
	for character in range(passwordLength):
		if whatToInsertIndex % 3 == 0:
			character = random.choice(capitalLetters)
		elif whatToInsertIndex % 3 == 1:
			character = random.choice(nonCapitalLetters)
		else:
			character = str(random.randint(0,9))
		character
		newPassword += character
		whatToInsertIndex += 1
	return newPassword

def PressTabTwice():
	pyautogui.hotkey("tab")
	pyautogui.hotkey("tab")

def FillInUserName(username):
	pyautogui.click(904,673)
	#time.sleep(1)
	pyautogui.typewrite(username)

def FillInPassword(password):
	pyautogui.typewrite(password)
	PressTabTwice()
	pyautogui.typewrite(password)

	
def CreateProtonAccount():
	CheckLoading("pm-loader-fullpage")
	userName = RandomUserNameGenerator(RandomNameGenerator())
	password = RandomPasswordGenerator(12)
	#clicks fullscreen
	pyautogui.click(1236,30)
	time.sleep(1)
	FillInUserName(userName)
	PressTabTwice()
	FillInPassword(password)
	#gets to "Create Account"
	PressTabTwice()
	PressTabTwice()
	pyautogui.hotkey("enter")
	#press confirm
	pyautogui.hotkey("enter")

	#KOM IGENNEM CAPTCHA. TJEK:
	#https://github.com/amjadsibili/EyeBot/blob/master/main.py

	


GetToProtonMailSignUp()
CreateProtonAccount()

#brug pyperclip til sidst. kopier brugernavn, password