import requests
import sys
import time
from selenium.webdriver.common.by import By
from pathlib import Path

# adapted from http://stackoverflow.com/questions/20716842/python-download-images-from-google-image-search
from selenium import webdriver

DRIVER_PATH = '../../TelegramBot/chromedriver.exe'
wd = webdriver.Chrome(executable_path=DRIVER_PATH)

def downloadImages(query_item, num_images, directory):
	list = fetch_image_urls(query_item, num_images)
	Path(directory).mkdir(parents=True, exist_ok=True)

	i=0
	for a in list:
		response = requests.get(a)
		time.sleep(1)
		file = open(directory+"/"+str(i)+".jpg", "wb")
		file.write(response.content)
		file.close()
		i = i + 1


def fetch_image_urls(query: str, max_links_to_fetch: int, wd: webdriver = wd, sleep_between_interactions: int = 1):
	def scroll_to_end(wd):
		wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(sleep_between_interactions)

	# build the google query
	search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

	# load the page
	wd.get(search_url.format(q=query))

	image_urls = set()
	image_count = 0
	results_start = 0
	while image_count < max_links_to_fetch:
		scroll_to_end(wd)

		# get all image thumbnail results
		thumbnail_results = wd.find_elements(By.CSS_SELECTOR, " img.Q4LuWd")
		number_results = len(thumbnail_results)
		print(thumbnail_results)
		print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")

		for img in thumbnail_results[results_start:number_results]:
			# try to click every thumbnail such that we can get the real image behind it
			try:
				img.click()
				time.sleep(sleep_between_interactions)
			except Exception:
				continue

			# extract image urls
			actual_images = wd.find_elements(By.CSS_SELECTOR, ' img.Q4LuWd')
			for actual_image in actual_images:
				if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
					image_urls.add(actual_image.get_attribute('src'))

			image_count = len(image_urls)

			if len(image_urls) >= max_links_to_fetch:
				print(f"Found: {len(image_urls)} image links, done!")
				break

		# move the result startpoint further down
		results_start = len(thumbnail_results)
	print(image_urls)
	return image_urls

if __name__ == '__main__':
	from sys import argv
	try:
		downloadImages(argv)
	except KeyboardInterrupt:
		pass
	sys.exit()