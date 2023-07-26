import logging

from selenium.webdriver.common.by import By


class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        input_miasto_xpath = "/html/body/div[5]/section/div[2]/div/div/div[2]/div/div[1]/form/div[1]/div/div[2]/a/span[1]"
        self.search_hotel_span = input_miasto_xpath
        self.search_hotel_input = "/html/body/div[17]/div/input"
        self.location_match_xpath = "/html/body/div[17]/ul/li/ul/li/div/span"
        self.check_in_input_name = "checkin"
        self.check_out_input_name = "checkout"
        self.travelers_input_id = "travellersInput"
        self.adult_input_id = "adultInput"
        self.child_input_id = "childInput"
        self.search_button_xpath = "/html/body/div[5]/section/div[2]/div/div/div[2]/div/div[1]/form/div[5]/button"
        self.logger = logging.getLogger(__name__)

    def set_city(self, city):
        self.logger.info(f"Setting city {city}")
        self.driver.find_element(By.XPATH, self.search_hotel_span).click()
        self.driver.find_element(By.XPATH, self.search_hotel_input).send_keys(city)
        self.driver.find_element(By.XPATH, self.location_match_xpath).click()

    def set_check_in(self, date):
        self.logger.info(f"Setting check in date: {date}")
        self.driver.find_element(By.NAME, self.check_in_input_name).send_keys(date)

    def set_check_out(self, date):
        self.logger.info(f"Setting check out date: {date}")
        self.driver.find_element(By.NAME, self.check_out_input_name).send_keys(date)

    def travelers(self, adult, child):
        self.logger.info(f"Setting travelers, adult: {adult}, child: {child}")

        self.driver.find_element(By.ID, self.travelers_input_id).click()
        self.driver.find_element(By.ID, self.adult_input_id).clear()
        self.driver.find_element(By.ID, self.adult_input_id).send_keys(adult)
        self.driver.find_element(By.ID, self.child_input_id).clear()
        self.driver.find_element(By.ID, self.child_input_id).send_keys(child)

    def search(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
