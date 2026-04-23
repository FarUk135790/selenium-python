import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCreateEventUnauthorized(unittest.TestCase):

    def setUp(self):
        # Preconditions
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")

    def test_create_event_unauthorized(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Натиснути на кнопку "Події"
        events_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/app-root/app-main/div/app-header/header/div[2]/div/div/nav/ul/li[2]/a")
        ))
        events_button.click()

        # Перевірка: вкладка "Події" відкрилась
        wait.until(EC.url_contains("events"))
        self.assertIn("events", driver.current_url)

        # Step 2: Натиснути на кнопку "Створити подію"
        create_event_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/app-root/app-main/div/div[2]/app-greencity-main/app-events/div/app-events-list/div/div/div[1]/div[2]/button")
        ))
        create_event_button.click()

        # Очікування модального вікна авторизації
        login_modal = wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="mat-mdc-dialog-4"]/div/div/app-auth-modal/div/div')
        ))

        # Перевірка: модальне вікно авторизації відображається
        self.assertTrue(login_modal.is_displayed())

    def tearDown(self):
        self.driver.quit()
