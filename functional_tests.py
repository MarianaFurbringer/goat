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

        # Ela é convidada a inserir um item de tarefa imediatamente
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # Ela digita "Buy peacock feathers" em uma caixa de texto
        # (O hobby de Edith é amarrar iscas de pesca com mosca)
        inputbox.send_keys("Buy peacock feathers")

        # Quando ela pressiona enter, a página é atualizada, e agora a página lista
        # "1: Buy peacock feathers" como um item em uma tabela de lista de tarefas
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(
            any(row.text == "1: Buy peacock feathers" for row in rows),
            "New to-do item did not appear in table",
    )

        # Ainda há uma caixa de texto convidando-a a adicionar outro item.
        # Ela digita "Use peacock feathers to make a fly"
        # (Edith é muito metódica)
        self.fail("Finish the test!")


if __name__ == "__main__":
    unittest.main()
