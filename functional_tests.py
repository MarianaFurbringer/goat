from selenium import webdriver

# Inicializar o navegador (certifique-se de que o geckodriver está no PATH)
browser = webdriver.Firefox()

# Abrir a URL
browser.get("http://localhost:8000")

# Verificar se "Congratulations!" está no título da página
assert "Congratulations!" in browser.title, "Texto não encontrado no título da página"

print("OK")