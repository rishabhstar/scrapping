from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import csv
driver=webdriver.Chrome()
driver.get(url="https://downtowndallas.com/experience/stay/")
placebutton =driver.find_element_by_class_name("place-square__btn")

action = ActionChains(driver)
action.click()
action.click(on_element= placebutton )
action.perform()
name=driver.find_element_by_class_name("place-name").text
image_url=driver.find_element_by_class_name("place-info-image").find_element_by_tag_name("img").get_attribute("src")
image=requests.get(image_url)
address_element=driver.find_elements_by_class_name("place-info-address")
address=address_element[0].text
telephone=address_element[1].text
area=address_element[2].text
driver.get(image_url)
driver.get_screenshot_as_file("F:/pychar/pycaharm/scrapping/images/image.png")
file=open("data.csv","w")
csvwriter=csv.writer(file)
column=["Name","image_url","Adress","phone","area"]
csvwriter.writerow(column)
csvwriter.writerow([name,image_url,address,telephone,area])
file.close()
driver.close()




