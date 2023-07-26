import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from anetka1.kurs_python.page_object_hotel.search_hotel import SearchHotelPage
from anetka1.kurs_python.page_object_hotel.search_result import SearchResultsPage


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("http://www.kurs-selenium.pl/demo/")
    driver.maximize_window()
    yield
    driver.quit()


def test_wejscie_na_strone(test_setup):
    assert driver.title == "PHPTRAVELS | Travel Technology Partner"


def test_hotel_search(test_setup):
    hotel_search = SearchHotelPage(driver)
    hotel_search.set_city("Dubai")
    hotel_search.set_check_in("25/07/2023")
    hotel_search.set_check_out("27/07/2023")
    hotel_search.travelers(adult=4, child=7)
    hotel_search.search()

    hotel_results = SearchResultsPage(driver)
    lista_hoteli = hotel_results.get_hotel_names()
    ceny = hotel_results.get_hotel_prices()

    assert lista_hoteli[0] == "Jumeirah Beach Hotel"
    assert lista_hoteli[1] == "Oasis Beach Tower"
    assert lista_hoteli[2] == "Rose Rayhaan Rotana"
    assert lista_hoteli[3] == "Hyatt Regency Perth"
    assert ceny[0] == "$22"
    assert ceny[1] == "$50"
    assert ceny[2] == "$80"
    assert ceny[3] == "$150"
