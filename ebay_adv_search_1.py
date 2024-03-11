from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
import time

class AdvanceSearch:
    def __init__(self):
        # set Firefox options
        self.options = Options()
        # print(dir(Options))
        # self.options.add_argument("--headless") # not to open the browser

        self.driver = webdriver.Firefox(options=self.options)

        self.f = open('ebay_search_log.log',"w+")

        self.driver.get("https://www.ebay.com/")

        self.f.write("\n>>>>>>>>>>>> Title <<<<<<<<<<<<<<<\n")
        self.f.write(f"{self.driver.title}\n")

        self.adv_search = self.driver.find_element(By.ID, "gh-as-a")
        self.f.write("\nEntered in Advance Search")
        self.adv_search.click()

    def find_element(self):
        time.sleep(1)
        self.kw_field = self.driver.find_element(By.ID, "_nkw")
        self.kw_field.send_keys("GoPro")
        self.f.write(f"\nEntered keyword : GoPro")

        time.sleep(1)
        self.kw_options = Select(self.driver.find_element(By.ID, "s0-1-17-4[0]-7[1]-_in_kw"))
        self.kw_options.select_by_value('3')
        self.f.write("\nKeyword Options : Exact words, exact order")

        time.sleep(1)
        self.ex_kw = self.driver.find_element(By.ID, "_ex_kw")
        self.ex_kw.send_keys("extreme teperature")
        self.f.write("\nExclude words from search : extreme temperature")

        time.sleep(1)
        self.all_cat = Select(self.driver.find_element(By.ID, "s0-1-17-4[0]-7[3]-_sacat"))
        self.all_cat.select_by_value('625')
        self.f.write("\nIn This Category : Cameras & Photo")

        time.sleep(1)
        self.search_inc = self.driver.find_element(By.XPATH, "//fieldset[@class='adv-fieldset__searchIncluding']//div[1]//span[1]//input[1]")
        self.search_inc.send_keys(Keys.SPACE)
        self.f.write("\nSrach Including : Title and description")
 
        time.sleep(1)
        self.price = self.driver.find_element(By.ID, "s0-1-17-5[2]-@range-comp[]-@range-textbox[]-textbox")
        self.price.send_keys("100", Keys.TAB, "500")
        self.f.write("\nPrice : Min $100 to Max $500")

        time.sleep(1)
        self.buy_format = self.driver.find_element(By.ID, "s0-1-17-6[3]-[1]-LH_Auction")
        self.f.write("\nBuying Format : Auction")
        self.buy_format.click()

        time.sleep(1)
        self.condition = self.driver.find_element(By.ID, "s0-1-17-6[4]-[0]-LH_ItemCondition")
        self.f.write("\nCondition : New")
        self.condition.click()

        time.sleep(1)
        self.show_Result = self.driver.find_element(By.ID, "s0-1-17-5[5]-[0]-LH_FR")
        self.f.write("\nShow Reslt : Free Returns")
        self.show_Result.click()

        time.sleep(1)
        self.shipping_opt = self.driver.find_element(By.ID, "s0-1-17-5[6]-[0]-LH_FS")
        self.f.write("\nShipping Options : Free Shipping")
        self.shipping_opt.click()

        time.sleep(1)
        self.item_loc = self.driver.find_element(By.ID, "s0-1-17-6[7]-[1]-LH_PrefLoc")
        self.f.write("\nItem Location : US Only")
        self.item_loc.click()

        time.sleep(1)
        self.sort_by = Select(self.driver.find_element(By.ID, "s0-1-17-8[9]-1[0]-_sop"))
        self.sort_by.select_by_value('15')
        self.f.write("\nSort By : Price + Shipping: lowest first")
    
        time.sleep(1)
        self.view_results = Select(self.driver.find_element(By.ID, "s0-1-17-8[9]-1[1]-_dmd"))
        self.view_results.select_by_value('2')
        self.f.write("\nView Results : Gallery view")

        time.sleep(1)
        self.res_per_page = Select(self.driver.find_element(By.ID, "s0-1-17-8[9]-1[2]-_ipg"))
        self.res_per_page.select_by_value('60')
        self.f.write("\nResults Per Page : 60")

        time.sleep(2)
        self.submit = self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn--primary']")
        self.submit.send_keys(Keys.ENTER)

    def close(self):
        print("Done")    
        time.sleep(2)
        self.driver.quit()


adv = AdvanceSearch()
adv.find_element()
adv.close()

