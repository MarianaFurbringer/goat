from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith acessa a página inicial e acidentalmente tenta submeter um item vazio
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # A página inicial é atualizada e pede que o campo não esteja em branco
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has-error').text,
            "You can't have an empty list item"
        ))

        # Ela tenta novamente com um texto para o item e isso funciona
        self.browser.find_element(By.ID, "id_new_item").send_keys("Buy milk")
        self.browser.find_element(By.ID, "id_new_item").send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")

        # Agora ela tenta colocar um segundo item em branco na lista
        self.browser.find_element(By.ID, "id_new_item").send_keys(Keys.ENTER)

        # Recebe mensagem de erro
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has-error').text,
            "You can't have an empty list item"
        ))

        # E ela pode corrigir isso preenchendo o item com um texto
        self.browser.find_element(By.ID, 'id_new_item').send_keys('Make tea')
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')
