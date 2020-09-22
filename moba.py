#TO DO:
#Pause video
#tjek hvis den emd mest views ikke er rigtig lane

import sys,time
from selenium import webdriver

#variables:
secondsToLook = 100
buildsToCheck = 15
not_matched = True
not_cookies = True

browser = webdriver.Chrome()



def GetToMoba():
	browser.get("https://www.google.com/search?q=" + champion + "+" + "mobafire&rlz=1C1CHBF_daGB898GB898&oq=hej+med+dig&aqs=chrome..69i57.1464j0j9&sourceid=chrome&ie=UTF-8")
	moba_elem = browser.find_element_by_partial_link_text("Mobafire")
	moba_elem.click()

def FindParents():
	list_of_all_parents = browser.find_elements_by_class_name("browse-list__item ")
	print(list_of_all_parents)
	sliced_parent_list = list_of_all_parents[0:buildsToCheck]
	return sliced_parent_list
	
def FindViews(sliced_parent_list):
	list_of_all_views = []
	for build in FindParents():
		rating_section = build.find_element_by_class_name("browse-list__item__rating")
		view_section = rating_section.find_element_by_class_name("browse-list__item__rating__views")
		view_list_work_in_progress = view_section.text.split(" ")
		views_with_commas = view_list_work_in_progress[1]
		views = views_with_commas.replace(",","")
		print(views)
		list_of_all_views.append(views)
	return list_of_all_views



def EnterGuide(button_to_press):
	button_to_press.click()
	global not_matched
	not_matched = False

def CheckRole(parent_to_check):
	correct_class_name = "role-" + lane
	check_role = parent_to_check.find_elements_by_class_name(correct_class_name)
	if len(check_role) != 0:
		EnterGuide(parent_to_check)
	else:
		pass




def AcceptCookies():
	accept_button = browser.find_element_by_css_selector("#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-overlay.qc-cmp2-footer-scrolled > div > button.sc-bwzfXH.bsCDNw")
	accept_button.click()

def CheckForCookies():
	accept_button = browser.find_elements_by_css_selector("#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-overlay.qc-cmp2-footer-scrolled > div > button.sc-bwzfXH.bsCDNw")
	if len(accept_button) > 0:
		global not_cookies
		not_cookies = False



if len(sys.argv) > 1:
	champion = str(sys.argv[1])
	lane = str(sys.argv[2])
	if lane == "mid":
		lane = "middle"
	elif lane == "supp":
		lane = "support"
	elif lane == "bot":
		lane = "bottom"
	GetToMoba()
	sliced_parent_list = FindParents()
	list_of_all_views = FindViews(sliced_parent_list)
	while not_cookies:
		CheckForCookies()
		time.sleep(0.1)
	else:
		AcceptCookies()
	
	
	while len(list_of_all_views) > 0 or not_matched:
		parent_index = list_of_all_views.index(max(list_of_all_views,key=int))
		check_match = sliced_parent_list[parent_index]
		CheckRole(check_match)
		del(list_of_all_views[parent_index])
	time.sleep(secondsToLook)

