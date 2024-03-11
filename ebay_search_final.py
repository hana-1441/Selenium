from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class AdvanceSearch:

    def __init__(self):
        self.f = open('ebay_search_log.log',"w+")
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.ebay.com/")
        self.f.write("\n>>>>>>>>>>>> Title <<<<<<<<<<<<<<<\n")
        self.f.write(f"{self.driver.title}\n")
        self.driver.find_element(By.ID, "gh-as-a").click()
        self.f.write("\nEntered in Advance Search\n")

    def send_key(self,element,title,data,*args):
        try:
            element.send_keys(*args)
        except:
            pass

        if data!=None:
            self.f.write(f"\n{title} : {data}")
        else:
            self.f.write(f"\n{title} : {args}")
        time.sleep(2)

    def all_elements(self):
        kw_item = self.driver.find_element(By.ID, "_nkw")
        self.send_key(kw_item,"Entered keyword",None,"GoPro")

        kw_options = self.driver.find_element(By.ID, "s0-1-17-4[0]-7[1]-_in_kw")
        self.send_key(kw_options,"Keyword Options",None,"Exact words, exact order")

        ex_kw = self.driver.find_element(By.ID, "_ex_kw")
        self.send_key(ex_kw,"Exclude words from search",None,"extreme teperature")

        all_cat = self.driver.find_element(By.ID, "s0-1-17-4[0]-7[3]-_sacat")
        self.send_key(all_cat,"In This Category",None,"Cameras & Photo")

        search_inc = self.driver.find_element(By.XPATH, "//fieldset[@class='adv-fieldset__searchIncluding']//div[1]//span[1]//input[1]").click()
        self.send_key(None,"Srach Including","Title and description",None)

        price = self.driver.find_element(By.ID, "s0-1-17-5[2]-@range-comp[]-@range-textbox[]-textbox")
        self.send_key(price,"Price","Min $100 to Max $500","100", Keys.TAB, "500")

        buy_format = self.driver.find_element(By.ID, "s0-1-17-6[3]-[1]-LH_Auction").click()
        self.send_key(None,"Buying Format","Auction",None)

        condition = self.driver.find_element(By.ID, "s0-1-17-6[4]-[0]-LH_ItemCondition").click()
        self.send_key(None,"Condition","New",None)

        show_Result = self.driver.find_element(By.ID, "s0-1-17-5[5]-[0]-LH_FR")
        self.send_key(show_Result,"Show Reslt","Free Returns",Keys.SPACE)

        shipping_opt = self.driver.find_element(By.ID, "s0-1-17-5[6]-[0]-LH_FS").click()
        self.send_key(None,"Shipping Options","Free Shipping",None)

        item_loc = self.driver.find_element(By.ID, "s0-1-17-6[7]-[1]-LH_PrefLoc").click()
        self.send_key(None,"Item Location","US Only",None)

        seller = self.driver.find_element(By.ID, "s0-1-17-8[9]-1[0]-_sop")
        self.send_key(seller,"Seller","Sort By : Price + Shipping: lowest first | View Results : Gallery view | Results Per Page : 60","Price + Shipping: lowest first", Keys.ENTER, Keys.TAB, "Gallery view", Keys.ENTER, Keys.TAB, "60")

        submit = self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn--primary']").click()

    def close(self):
        time.sleep(4)
        self.driver.quit()


obj = AdvanceSearch()
obj.all_elements()
obj.close()