from selenium import webdriver
import urllib.request
import time
import os
from tkinter import filedialog

namesFilePath = 'C:/Users/NF/Documents/project1/Scrape-GettyImages-Using-Selenium/names.txt'
gettyURL = 'https://www.gettyimages.ae/photos/first-last?family=editorial&phrase=first%20last&sort=mostpopular#license'
newImagesPath = 'C:/Users/NF/Documents/project1/Scrape-GettyImages-Using-Selenium/images'
pages = 5
list_of_names = []


def download_image(person_name, src, seq, dir):
    try:
        filename = person_name + str(seq) + '.png' # i.e: "JohnTravolta0.png"
        image_path = os.path.abspath(os.path.join(os.getcwd(), dir, filename)) # /home/user/Desktop/dirname
        urllib.request.urlretrieve(src, image_path) # download image
    
    except Exception:
        pass

def getNames():
  with open(namesFilePath) as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split(',')]
        for i in inner_list: 
          list_of_names.append(i)

        
def getURL(name):
  if len(name.split()) > 1: 
     first = name.split()[0]
     last = name.split()[1]
     url = gettyURL.replace('first',first).replace('last',last)
     return url
  else: 
    first = name.split()[0]
    url = gettyURL.replace('first',first).replace('last','').replace('%20','').replace('-?','?')
    return url

def create_folder(name):
  if newImagesPath == '': 
    folderPath = filedialog.askdirectory()
    folderPath = os.path.join(folderPath,name)
  else: 
    folderPath = os.path.join(newImagesPath,name)
  if not os.path.isdir(folderPath): # If the folder does not exist in working directory, create a new one.
        os.makedirs(folderPath)
  return folderPath
  


def browse_page(person_name, pages,driver, dir):
    seq = 0 #initialize the file number. 
    for i in range(pages): # Loop for the number of pages you want to scrape.
        try:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') # Scroll to the end of page.
            time.sleep(2) # Wait for all the images to load correctly.
            images = driver.find_elements_by_xpath("//img[contains(@class, 'gallery-asset__thumb gallery-mosaic-asset__thumb')]") # Find all images.
        except:
            continue

        for image in images: # For each image in one page:
              try:
                src = image.get_attribute('src') # Get the link
                download_image(person_name, src, seq, dir) # And download it to directory
              except:
                pass
              seq += 1
        try:
          nextpage = driver.find_element_by_css_selector('.search-pagination__button-icon--next').click() # Move to next page
        except:
          pass
        time.sleep(2)
 

def getImages():
    getNames()
    driver.maximize_window()
    for i in list_of_names: 
      driver.get(getURL(i))
      dirc = create_folder(i)
      browse_page(i, pages,driver, dirc)


	
driver = webdriver.Chrome('C:/Users/NF/chromedriver.exe') # IF YOU ARE USING CHROME.
#driver = webdriver.Firefox() # IF YOU ARE USING Firfox.
getImages()