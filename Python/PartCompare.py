from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

a = input("What are the CPUs or GPUs to compare, separated by commas?\n").split(',')
gpu1 = a[0]
gpu2 = a[1]

opts = webdriver.ChromeOptions()
opts.add_extension('ublock.crx')
driver = webdriver.Chrome("C:\Extra\chromedriver\chromedriver.exe",chrome_options=opts)
driver.get("http://www.google.com")
elem = driver.find_element_by_name("q")
elem.send_keys("site:userbenchmark.com {0} vs {1}".format(gpu1,gpu2))
elem.send_keys(Keys.RETURN)
link = 0
while not link:
    try:
        link = driver.find_elements_by_css_selector("#rso div div h3")[0]
    except IndexError:
        continue
link.click()
try:
    rank1 = driver.find_elements_by_css_selector(".innercolleft")[0].text
    rank2 = driver.find_elements_by_css_selector(".innercolright")[0].text
    gpu1 = driver.find_element_by_css_selector("#select2-chosen-1").text
    gpu2 = driver.find_element_by_css_selector("#select2-chosen-2").text
    if rank1:
        print("The {0} scored {1} better than the {2}.".format(gpu1,rank1,gpu2))
    else:
        print("The {0} scored {1} better than the {2}.".format(gpu2,rank2,gpu1))
except IndexError:
    print("There was an issue finding the results.")
driver.quit()
