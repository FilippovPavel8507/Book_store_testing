from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#Настроить открытие окон в полный размер
driver.maximize_window()
#Реализовать неявное ожидание поиска элементов
driver.implicitly_wait(5)
#Открыть страницу https://practice.automationtesting.in/
driver.get("https://practice.automationtesting.in/")
#Проскролить страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
#Нажать на название книги "Selenium Ruby" или на кнопку "READ MORE"
Selenium_Ruby = driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0")
Selenium_Ruby.click()
#Нажать на вкладку "REVIEWS"
rewiews = driver.find_element_by_css_selector("li.reviews_tab")
rewiews.click()
#Поставить 5 звёзд
stars = driver.find_element_by_css_selector("a.star-5")
stars.click()
#Заполнить поле "Review" сообщением: "Nice book!"
rewiew_field = driver.find_element_by_css_selector("#comment")
rewiew_field.send_keys("Nice book!")
#Заполнить поле "Name"
name_field = driver.find_element_by_css_selector("#author")
name_field.send_keys("Pavel")
#Заполнить "E-mail"
Email_field = driver.find_element_by_css_selector("#email")
Email_field.send_keys("pavelfilippov8507@gmail.com")
#Нажать на кнопку "SUBMIT"
submit_btn = driver.find_element_by_css_selector("#submit")
submit_btn.click()
#Закрываем автотест
driver.quit()