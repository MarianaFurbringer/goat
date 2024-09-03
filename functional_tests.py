from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        # Inicializa o navegador Chrome
        self.browser = webdriver.Chrome()  # Alterado para Chrome

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        # Edith ouviu falar de um novo aplicativo de lista de tarefas.
        # Ela vai conferir a página inicial
        self.browser.get("http://localhost:8000")

        # Ela nota que o título da página e o cabeçalho mencionam listas de tarefas
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly"
        # (Edith is very methodical)
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(
            "1: Buy peacock feathers",
            [row.text for row in rows],
        )
        self.assertIn(
            "2: Use peacock feathers to make a fly",
            [row.text for row in rows],
        )

        # Satisfied, she goes back to sleep