from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class FetchData:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.w3schools.com/')

        self.driver.find_element(By.LINK_TEXT,'PYTHON').click()

        self.slider = self.driver.find_element(By.XPATH , "//div[@id='leftmenuinnerinner']")

        self.items = self.slider.find_elements(By.PARTIAL_LINK_TEXT, "Python")

        self.titles = []

    def total_data(self,d_count):
        for i in range(d_count):
            self.titles.append(self.items[i].text)

    def make_dir(self):
        for i in self.titles:
            try:
                os.mkdir(i)
                selective_source = self.driver.find_element(By.CSS_SELECTOR, "#main").get_attribute("innerHTML")
                x=1
                self.driver.execute_script("window.scrollTo(0,4000)")
                examples = self.driver.find_elements(By.XPATH, "//div[@class='w3-code notranslate pythonHigh']")
                for ex in examples:
                    f2 = open(f"{i}/example{x}.py",'w')
                    f2.write(ex.text)
                    f2.close()
                    x+=1

                f1 = open(f"{i}/file.html",'w')
                f1.write(selective_source)
                f1.close()

                time.sleep(2)
                next = self.driver.find_elements(By.CSS_SELECTOR, "a[class='w3-right w3-btn']")
                next[1].click()
                time.sleep(2)
            except:
                pass

    def finish(self):
        self.driver.quit()

obj1 = FetchData()
obj1.total_data(5)
obj1.make_dir()
obj1.finish()        


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>if not classified <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# driver = webdriver.Firefox()
# driver.get('https://www.w3schools.com/')

# driver.find_element(By.LINK_TEXT,'PYTHON').click()

# slider = driver.find_element(By.XPATH , "//div[@id='leftmenuinnerinner']")

# items = slider.find_elements(By.PARTIAL_LINK_TEXT, "Python")

# titles = []

# def total_data(x):
#     for i in range(x):
#         titles.append(items[i].text)


# for i in titles:
#     os.mkdir(i)
#     selective_source = driver.find_element(By.CSS_SELECTOR, "#main").get_attribute("innerHTML")
#     x=1
#     driver.execute_script("window.scrollTo(0,4000)")
#     examples = driver.find_elements(By.XPATH, "//div[@class='w3-code notranslate pythonHigh']")
#     for ex in examples:
#         f2 = open(f"{i}/example{x}.py",'w')
#         f2.write(ex.text)
#         f2.close()
#         x+=1

#     f1 = open(f"{i}/file.html",'w')
#     f1.write(selective_source)
#     f1.close()

#     next = driver.find_elements(By.CSS_SELECTOR, "a[class='w3-right w3-btn']")
#     next[1].click()
#     time.sleep(1)

# print("Done")
# driver.close()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>> If want to scroll in several chunks (slow scroll of page)  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# p1=0 #start point of scroll
# p2=800 #end point of scroll

# for i in range(5):
#     driver.execute_script(f"window.scrollTo({p1},{p2})")
#     p1=p2
#     p2+=800
#     time.sleep(0.5)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<