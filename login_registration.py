from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#Настроить открытие окон в полный размер
driver.maximize_window()
#Реализовать неявное ожидание поиска элементов
driver.implicitly_wait(5)
#Открыть страницу https://practice.automationtesting.in/
driver.get("https://practice.automationtesting.in/")
#Нажать на вкладку "My Account"
My_Account = driver.find_element_by_css_selector("#menu-item-50 > a")
My_Account.click()
#В разделе "Register", введите e-mail для регистрации
Email_field = driver.find_element_by_css_selector("#reg_email")
Email_field.send_keys("pavelfilippov8507@gmail.com")
#В разделе "Register", введите пароль для регистрации
#составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
#почту и пароль сохраните, потребуются в дальнейшем
Password_field = driver.find_element_by_css_selector("#reg_password")
Password_field.send_keys("89603550993fpa!")
#Нажмите на кнопку "Register"
register_btn = driver.find_element_by_css_selector("p.woocomerce-FormRow.form-row > input.woocommerce-Button.button")
register_btn.click()
#Закрываем автотест
driver.quit()


from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#Настроить открытие окон в полный размер
driver.maximize_window()
#Реализовать неявное ожидание поиска элементов
driver.implicitly_wait(5)
#Открыть страницу https://practice.automationtesting.in/
driver.get("https://practice.automationtesting.in/")
#Нажать на вкладку "My Account"
My_Account = driver.find_element_by_css_selector("#menu-item-50 > a")
My_Account.click()
#В разделе "Login", введите email для логина
Email_field = driver.find_element_by_css_selector("#username")
Email_field.send_keys("pavelfilippov8507@gmail.com")
#В разделе "Login", введите пароль для логина
Password_field = driver.find_element_by_css_selector("#password")
Password_field.send_keys("89603550993fpa!")
#Нажмите на кнопку "Login"
register_btn = driver.find_element_by_css_selector("p:nth-child(3)")
register_btn.click()
#Добавьте проверку, что на странице есть элемент "Logout"
logout = driver.find_element_by_tag_name("-customer-logout")
logout.click()
# Подтверждение и проверка элемента
logout = driver.switch_to.logout
logout_expected_text = "logout"
logout_text = logout.text
#Закрываем автотест
driver.quit()