import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTelegramButton(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")

    def test_telegram_button(self):
        driver = self.driver

        # Знаходимо кнопку (більш стабільний XPath)
        telegram_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button//img[contains(@src, 'telegram')]"))
        )

        self.assertTrue(telegram_button.is_displayed(), "Іконка Telegram не відображається")

        # Клік
        telegram_button.click()

        # Чекаємо зміну URL або нову вкладку
        self.wait.until(lambda d: "telegram" in d.current_url or len(d.window_handles) > 1)

        # Якщо відкрилась нова вкладка
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[1])

        current_url = driver.current_url
        self.assertTrue("t.me" in current_url or "telegram" in current_url,
                        "Telegram не відкрився")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
