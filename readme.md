- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Usage](#usage)
- [License](#license)

# Scrape Images From GETTYIMAGES.COM

## introduction

Thanks to the developer of this awesome tool for uploading photos from gettyImages.com. I added my own touch to the tool to help me collect data sets for the graduation project.
i add to this project :
* you can download a lot of images, just but they name to 'names.txt' 
* you don't need to but URL for every person  
* directory for all images, and it's classified with names 

## About The Project

The goal of this project is to scrape images from GettyImages.com and use them for classification purposes. The images are not in full resolution since to do that one would need an account. However, for my little project I do not need high-quality images and as such, I will download the photos that are presented once a query has been submitted.

## Getting Started

In order to successfully run the codes, you need to follow the steps below.

### Prerequisites

The packages that will be used are the following:

``` python
from selenium import webdriver
import urllib.request
import time
import os
from tkinter import filedialog
```

### Usage

Download Scraper.py file and place it under your desired directory. 

first of all, open the names.txt file, add whatever you want of names, just separated it with a comma (,)
in scraper.py there is 3 variable you might need to check them out 
* *namesFilePath*: the path to a names txt file
* *newImagesPath(optinal)*: if you will download many person images, just provide a folder that you want to but all images inside, every person will have a folder with he's name ( same name inside names.txt ). if you leave it empty '' it will ask you where you want to but the images 
* *pages*: Number of pages that you want to scrape from the website


Run the file by:

``` python
python scraper.py
```

go to make a cup of tea and come back will find all your images downloaded !

## Authors

* **Enes Ahmeti** - *Project developer & owner* - [KryeKuzhinieri](https://github.com/KryeKuzhinieri)
* **Nawaf Almuaither** - *developer* - [n2waf](https://github.com/n2waf)

## License

Distributed under the MIT License. See `LICENSE` for more information.
