from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(Service=service)

browser.get("https://dlp.hashtagtreinamentos.com/python/minicurso/minicurso-automacao/inscricao?curso=python&origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M")
browser.find_element('xpath', '//*[@id="BotaoPopup1"]').click()
browser.find_element('xpath', '//*[@id="firstname"]').send_keys("João")
browser.find_element('xpath', '//*[@id="email"]').send_keys("joao@gmail.com")
browser.find_element('xpath', '//*[@id="phone"]').send_keys("11999999999")
browser.find_element('xpath', '//*[@id="_form_1925_submit"]').click()

browser.quit()


