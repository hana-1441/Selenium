from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select  # for drop-down list
import time

driver = webdriver.Firefox()

driver.get("https://www.ebay.com/")

adv_search = driver.find_element(By.ID, "gh-as-a").click()

time.sleep(1)
kw_field = driver.find_element(By.ID, "_nkw")
kw_field.send_keys("GoPro", Keys.TAB)

time.sleep(1)
kw_options = Select(driver.find_element(By.ID, "s0-1-17-4[0]-7[1]-_in_kw"))
kw_options.select_by_value('3')

# Select is used for drop-down list selection 
# It has three methods given below : 
#   1) kw_options.select_by_value('value')
#   2) kw_options.select_by_index('index')
#   3) kw_options.select_by_visible_text('text_visible')

# the given below also works
# kw_options.send_keys("Exact words, exact order", Keys.ENTER, Keys.TAB)

time.sleep(1)
ex_kw = driver.find_element(By.ID, "_ex_kw")
ex_kw.send_keys("extreme teperature", Keys.TAB)

time.sleep(1)
all_cat = Select(driver.find_element(By.ID, "s0-1-17-4[0]-7[3]-_sacat"))
all_cat.select_by_value('625')
# all_cat.send_keys("Cameras & Photo", Keys.ENTER, Keys.TAB*3)

time.sleep(1)
search_inc = driver.find_element(By.XPATH, "//fieldset[@class='adv-fieldset__searchIncluding']//div[1]//span[1]//input[1]")
search_inc.send_keys(Keys.SPACE)

time.sleep(1)
price = driver.find_element(By.ID, "s0-1-17-5[2]-@range-comp[]-@range-textbox[]-textbox")
price.send_keys("100", Keys.TAB, "500")

time.sleep(1)
buy_format = driver.find_element(By.ID, "s0-1-17-6[3]-[1]-LH_Auction")
buy_format.send_keys(Keys.SPACE, Keys.TAB)

time.sleep(1)
condition = driver.find_element(By.ID, "s0-1-17-6[4]-[0]-LH_ItemCondition")
condition.send_keys(Keys.SPACE)


time.sleep(1)
show_Result = driver.find_element(By.ID, "s0-1-17-5[5]-[0]-LH_FR")
show_Result.send_keys(Keys.SPACE, Keys.TAB*9, "Started within",Keys.TAB, "24 hours", Keys.TAB*2, "10", Keys.TAB, "100", Keys.TAB*2, "2", Keys.TAB,"20")


time.sleep(1)
shipping_opt = driver.find_element(By.ID, "s0-1-17-5[6]-[0]-LH_FS")
shipping_opt.send_keys(Keys.SPACE, Keys.TAB)

time.sleep(1)
item_loc = driver.find_element(By.ID, "s0-1-17-6[7]-[1]-LH_PrefLoc")
item_loc.send_keys(Keys.SPACE, Keys.TAB)

time.sleep(1)
seller = driver.find_element(By.ID, "s0-1-17-8[9]-1[0]-_sop")
seller.send_keys("Price + Shipping: lowest first", Keys.ENTER, Keys.TAB, "Gallery view", Keys.ENTER, Keys.TAB, "60")

time.sleep(2)
submit = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn--primary']")
submit.send_keys(Keys.ENTER)

print("Done")    
time.sleep(10)
driver.quit()