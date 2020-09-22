import sys,time
from selenium import webdriver

secondsToLook = 60
not_cookies = True

browser = webdriver.Chrome()
def GetToMetasrc():
	browser.get("https://www.google.com/search?q=" + champion + "+" + "aram&rlz=1C1CHBF_daGB898GB898&oq=hej+med+dig&aqs=chrome..69i57.1464j0j9&sourceid=chrome&ie=UTF-8")
	moba_elem = browser.find_element_by_partial_link_text("METAsrc")
	moba_elem.click()

def AcceptCookies():
	accept_button = browser.find_element_by_css_selector("#onetrust-accept-btn-handler")
	accept_button.click()

def CheckForCookies():
	accept_button = browser.find_elements_by_css_selector("#onetrust-accept-btn-handler")
	if len(accept_button) > 0:
		global not_cookies
		not_cookies = False

def CheckGotIt():
	pass
def AcceptGotIt():
	pass


if len(sys.argv) > 1:
	champion = str(sys.argv[1])
	GetToMetasrc()
	while not_cookies:
		CheckForCookies()
		time.sleep(0.1)
	else:
		AcceptCookies()

	time.sleep(secondsToLook)