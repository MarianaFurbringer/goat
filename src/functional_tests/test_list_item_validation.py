
from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        #Edith acessa a página inicial e acidentalmente tenta submeter um item vazio

        #A página inicial é atualizada e pede que o campo não esteja em branco
        #Ela tentar novamente com um texto para o item
        #Agora ela tenta colocar um segundo item em branco na lista
        #Recebe mensagem de erro
        #E ela pode corrigir isso preenchendo o item com um texto
        self.fail("write me!")
    
        