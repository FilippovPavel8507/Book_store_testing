from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#Настроить открытие окон в полный размер
driver.maximize_window()
#Реализовать неявное ожидание поиска элементов
driver.implicitly_wait(5)
#Открыть страницу https://practice.automationtesting.in/
driver.get("https://practice.automationtesting.in/")
#Залогиниться
#1) Нажать на вкладку "My Account"
My_Account = driver.find_element_by_css_selector("#menu-item-50 > a")
My_Account.click()
#2) В разделе "Login", введите email для логина
Email_field = driver.find_element_by_css_selector("#username")
Email_field.send_keys("pavelfilippov8507@gmail.com")
#3) В разделе "Login", введите пароль для логина
Password_field = driver.find_element_by_css_selector("#password")
Password_field.send_keys("89603550993fpa!")
#4) Нажмите на кнопку "Login"
login_btn = driver.find_element_by_css_selector("p:nth-child(3)")
login_btn.click()
#Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()
#Откройте книгу "HTML 5 Forms"
book = driver.find_element_by_tag_name("li.post-181")
book.click()
#Добавьте тест, что заголовок книги называется: "HTML5 Forms"
HTML5_Forms = driver.find_element_by_css_selector("div.summary.entry-summary > h1")
HTML5_Forms_get_text = HTML5_Forms.text
assert "HTML5 Forms" in HTML5_Forms_get_text
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
#Залогиниться
#1) Нажать на вкладку "My Account"
My_Account = driver.find_element_by_css_selector("#menu-item-50 > a")
My_Account.click()
#2) В разделе "Login", введите email для логина
Email_field = driver.find_element_by_css_selector("#username")
Email_field.send_keys("pavelfilippov8507@gmail.com")
#3) В разделе "Login", введите пароль для логина
Password_field = driver.find_element_by_css_selector("#password")
Password_field.send_keys("89603550993fpa!")
#4) Нажмите на кнопку "Login"
login_btn = driver.find_element_by_css_selector("p:nth-child(3)")
login_btn.click()
#Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()
#Откройте категорию "HTML"
HTML = driver.find_element_by_css_selector("li.cat-item.cat-item-19 > a")
HTML.click()
#Добавьте тест, что отображается три товара
count = driver.find_element_by_css_selector("li.cat-item.cat-item-19.current-cat > span") #находим по селектору строку HTML-кода со значением "3"
count_3 = count.get_attribute("class") #указываем значение атрибута "class" из строки HTML-кода
if count_3 is None: #если значение НЕ пустое, значит атрибут "class" равен 3
    print("Не отображается 3 товара")
else:
    print("Отображается 3 товара")
#Закрываем автотест
driver.quit()


from selenium import webdriver
from selenium.webdriver.support.select import Select # импортируем драйвер Select для переключения в селекторе
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#Настроить открытие окон в полный размер
driver.maximize_window()
#Реализовать неявное ожидание поиска элементов
driver.implicitly_wait(5)
#Открыть страницу https://practice.automationtesting.in/
driver.get("https://practice.automationtesting.in/")
#Залогиниться
#1) Нажать на вкладку "My Account"
My_Account = driver.find_element_by_css_selector("#menu-item-50 > a")
My_Account.click()
#2) В разделе "Login", введите email для логина
Email_field = driver.find_element_by_css_selector("#username")
Email_field.send_keys("pavelfilippov8507@gmail.com")
#3) В разделе "Login", введите пароль для логина
Password_field = driver.find_element_by_css_selector("#password")
Password_field.send_keys("89603550993fpa!")
#4) Нажмите на кнопку "Login"
login_btn = driver.find_element_by_css_selector("p:nth-child(3)")
login_btn.click()
#Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()
#Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
menu_order = driver.find_element_by_css_selector("select > option:nth-child(1)") #находим по селектору строку HTML-кода со значением "Default sorting"
menu_order_default_sorting = count.get_attribute("selected") #указываем значение атрибута "selected " из строки HTML-кода
if menu_order_default_sorting is None: #если значение НЕ пустое, значит атрибут "selected" равен "Default sorting"
    print("Не выбрана сортировка по умолчанию")
else:
    print("Выбрана сортировка по умолчанию")
#отсортируйте товары по цене от большей к меньшей
#в селекторах используйте класс Select
menu_order_price = driver.find_element_by_name("orderby") #находим по селектору строку HTML-кода с атрибутом class "orderby", задающим все параметры сортировки
select = Select(menu_order_price) #указываем классу Select переменную в которой нужно выбрать селектор по цене от большей к меньшей
select.select_by_value("price") #указываем элемент с текстом "price" со значением "Sort by price: low to high"
#Снова объявите переменную с локатором основного селектора сортировки, т.к после сортировки страница обновится
menu_order = driver.find_element_by_name("orderby") #находим по селектору строку HTML-кода с атрибутом class "orderby", задающим все параметры сортировки
select = Select(menu_order) #указываем классу Select переменную в которой нужно выбрать селектор по цене от большей к меньшей
select.select_by_value("menu_order") #указываем элемент с текстом "menu_order" со значением "Default sorting"
#Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей. Используйте проверку по value
menu_order = driver.find_element_by_css_selector("select > option:nth-child(5)") #находим по селектору строку HTML-кода со значением "Sort by price: low to high"
menu_order_price = menu_order.get_attribute("value") #указываем значение атрибута "value" из строки HTML-кода
if menu_order_price is None: #если значение НЕ пустое, значит атрибут "value" равен "Sort by price: low to high"
    print("Выбрана сортировка по цене от большей к меньшей")
else:
    print("Не выбрана сортировка по цене от большей к меньшей") # в терминале должен отобразиться этот вариант, т.к. изначально выбрана сортировка с локатором основного селектора, т.е. по умолчанию
#Закрываем автотест
driver.quit()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#Настроить открытие окон в полный размер
driver.maximize_window()
#Реализовать неявное ожидание поиска элементов
driver.implicitly_wait(5)
#Открыть страницу https://practice.automationtesting.in/
driver.get("https://practice.automationtesting.in/")
#Залогиниться
#1) Нажать на вкладку "My Account"
My_Account = driver.find_element_by_css_selector("#menu-item-50 > a")
My_Account.click()
#2) В разделе "Login", введите email для логина
Email_field = driver.find_element_by_css_selector("#username")
Email_field.send_keys("pavelfilippov8507@gmail.com")
#3) В разделе "Login", введите пароль для логина
Password_field = driver.find_element_by_css_selector("#password")
Password_field.send_keys("89603550993fpa!")
#4) Нажмите на кнопку "Login"
login_btn = driver.find_element_by_css_selector("p:nth-child(3)")
login_btn.click()
#Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()
# Откройте книгу "Android Quick Start Guide"
book = driver.find_element_by_tag_name("li.post-169")
book.click()
#Добавьте тест, что содержимое старой цены = "^600.00" используйте assert
old_price = driver.find_element_by_css_selector("del > span")
old_price_get_text = old_price.text
assert "600.00" in old_price_get_text
#Добавьте тест, что содержимое новой цены = "^450.00" используйте assert
new_price = driver.find_element_by_css_selector("ins > span")
new_price_get_text = new_price.text
assert "450.00" in new_price_get_text
#Добавьте явное ожидание и нажмите на обложку книги, подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
book_cover = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#product-169 > div.images > a > img")))
book_cover = driver.find_element_by_css_selector("#product-169 > div.images > a > img")
book_cover.click()
#Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.pp_details > a")))
close = driver.find_element_by_css_selector("div.pp_details > a")
close.click()
#Закрываем автотест
driver.quit()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#Настроить открытие окон в полный размер
driver.maximize_window()
#Реализовать неявное ожидание поиска элементов
driver.implicitly_wait(5)
#Открыть страницу https://practice.automationtesting.in/
driver.get("https://practice.automationtesting.in/")
#Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()
#Добавьте в корзину книгу "HTML5 WebApp Development"
book = driver.find_element_by_tag_name("li.post-182") #Выбираем книгу "HTML5 WebApp Development"
book.click()
add_to_basket = driver.find_element_by_css_selector("form > button") #Добавляем книгу в корзину
add_to_basket.click()
#Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = ’’^180.00". Используйте для проверки assert
number_of_products = driver.find_element_by_css_selector("span.cartcontents") #задаем переменную для проверки количества товаров
number_of_products_get_text = number_of_products.text #указываем, что заданная переменная будет проверяться по содержанию текста
assert "1 Item" in number_of_products_get_text #указываем в кавычках значение из строки HTML-кода "1 Item", по которому будет проводиться проверка
cost = driver.find_element_by_css_selector("span.amount") #задаем переменную для проверки стоимости
cost_get_text = cost.text #указываем, что заданная переменная будет проверяться по содержанию текста
assert "₹180.00" in cost_get_text #указываем в кавычках значение из строки HTML-кода "₹180.00", по которому будет проводиться проверка
#Перейдите в корзину
basket = driver.find_element_by_css_selector("#wpmenucartli > a")
basket.click()
#Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
Subtotal = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.cart-subtotal > td > span"), "180.00"))
#Используя явное ожидание, проверьте что в Total отобразилась стоимость
Total = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.order-total > td > strong > span"), "183.60"))
#Закрываем автотест
driver.quit()


import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#Настроить открытие окон в полный размер
driver.maximize_window()
#Реализовать неявное ожидание поиска элементов
driver.implicitly_wait(5)
#Открыть страницу https://practice.automationtesting.in/
driver.get("https://practice.automationtesting.in/")
#Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()
#Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
driver.execute_script("window.scrollBy(0, 300);") #Перед добавлением первой книги, проскролльте вниз на 300 пикселей
book_1 = driver.find_element_by_tag_name("li.post-182") #Выбираем книгу "HTML5 WebApp Development"
book_1.click()
add_to_basket_1 = driver.find_element_by_css_selector("form > button") #Добавляем книгу в корзину
add_to_basket_1.click()
time.sleep(5) #После добавления 1-й книги добавьте sleep
shop = driver.find_element_by_css_selector("#menu-item-40 > a") #Возвращаемся в основной каталог
shop.click()
book_2 = driver.find_element_by_tag_name("li.post-180") #Выбираем книгу "JS Data Structures and Algorithm"
book_2.click()
add_to_basket_2 = driver.find_element_by_css_selector("form > button") #Добавляем книгу в корзину
add_to_basket_2.click()
#Перейдите в корзину
basket = driver.find_element_by_css_selector("#wpmenucartli > a")
basket.click()
#Удалите первую книгу
Delete_book_1 = driver.find_element_by_css_selector("tr:nth-child(1) > td.product-remove > a")
Delete_book_1.click()
#Нажмите на Undo (отмена удаления)
Undo = driver.find_element_by_css_selector("div.woocommerce-message > a")
Undo.click()
#В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
driver.find_element_by_css_selector("tr:nth-child(1) > td.product-quantity > div > input").clear() #Очищаем поле с количеством книг в корзине от значений
shop = driver.find_element_by_css_selector("#menu-item-40 > a") #Возвращаемся в основной каталог
shop.click()
book_3 = driver.find_element_by_tag_name("li.post-180") #Выбираем книгу "JS Data Structures and Algorithm"
book_3.click()
add_to_basket_3 = driver.find_element_by_css_selector("form > button") #Добавляем 1-ю книгу в корзину
add_to_basket_3.click()
add_to_basket_4 = driver.find_element_by_css_selector("form > button") #Добавляем 2-ю книгу в корзину
add_to_basket_4.click()
add_to_basket_5 = driver.find_element_by_css_selector("form > button") #Добавляем 3-ю книгу в корзину
add_to_basket_5.click()
basket = driver.find_element_by_css_selector("#wpmenucartli > a") #Переходим в корзину
basket.click()
#Нажмите на кнопку "UPDATE BASKET"
Update_basket = driver.find_element_by_name("update_cart")
Update_basket.click()
#Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3. Используйте assert
value = driver.find_element_by_css_selector("tr:nth-child(1) > td.product-quantity > div > input")
value_get_text = value.text
assert "3" in value_get_text
#Нажмите на кнопку "APPLY COUPON"
time.sleep(5) #Перед нажатием добавьте sleep
Apply_coupon = driver.find_element_by_css_selector("td > div > input.button")
Apply_coupon.click()
#Добавьте тест, что возникло сообщение: "Please enter a coupon code."
message = driver.find_element_by_css_selector("div.woocommerce > ul > li")
message_get_text = message.text
assert "Please enter a coupon code." in message_get_text
#Закрываем автотест


import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#Настроить открытие окон в полный размер
driver.maximize_window()
#Реализовать неявное ожидание поиска элементов
driver.implicitly_wait(1)
#Открыть страницу https://practice.automationtesting.in/
driver.get("https://practice.automationtesting.in/")
#Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()
#Добавьте в корзину книгу "HTML5 WebApp Development"
book = driver.find_element_by_tag_name("li.post-182") #Выбираем книгу "HTML5 WebApp Development"
book.click()
add_to_basket = driver.find_element_by_css_selector("form > button") #Добавляем книгу в корзину
add_to_basket.click()
#Перейдите в корзину
basket = driver.find_element_by_css_selector("#wpmenucartli > a")
basket.click()
#Нажмите "PROCEED TO CHECKOUT". Перед нажатием, добавьте явное ожидание
checkout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.cart-collaterals > div > div > a"))) #Добавляем явное ожидание по кликабельности кнопки.
checkout = driver.find_element_by_css_selector("div.cart-collaterals > div > div > a")
checkout.click()
#Заполните все обязательные поля. Перед заполнением first name, добавьте явное ожидание.
First_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#billing_first_name"))) #Добавляем явное ожидание по кликабельности поля.
First_name = driver.find_element_by_css_selector("#billing_first_name") #Находим по селектору поле ввода First_name
First_name.send_keys("Pavel") #Вводим имя
First_name.click()
Last_name = driver.find_element_by_css_selector("#billing_last_name") #Находим по селектору поле ввода Last_name
Last_name.send_keys("Filippov") #Вводим фамилию
Last_name.click()
Email = driver.find_element_by_css_selector("#billing_email") #Находим по селектору поле ввода Email
Email.send_keys("pavelfilippov8507@gmail.com") #Вводим Email
Email.click()
Phone = driver.find_element_by_css_selector("#billing_phone") #Находим по селектору поле ввода Phone
Phone.send_keys("89603550993") #Вводим номер телефона
Phone.click()
Select_country = driver.find_element_by_css_selector("#s2id_billing_country > a").click() #Нажимаем на селектор с выбором страны
Country_field = driver.find_element_by_css_selector("#s2id_autogen1_search") #Нажимаем на поле ввода страны
Country_field.send_keys("Russia") #Указываем в поле ввода название страны
Select_Russia = driver.find_element_by_class_name("select2-match").click() #Подтверждаем выбор страны
Address = driver.find_element_by_css_selector("#billing_address_1") #Находим по селектору поле ввода Address
Address.send_keys("Antonova street, 4, 65") #Вводим адрес проживания
Address.click()
City = driver.find_element_by_css_selector("#billing_city") #Находим по селектору поле ввода Town/City
City.send_keys("Saratov") #Вводим название города проживания
City.click()
State = driver.find_element_by_css_selector("#billing_state") #Находим по селектору поле ввода State/Country
State.send_keys("Saratovskaya oblast") #Вводим название области
State.click()
Postcode = driver.find_element_by_css_selector("#billing_postcode") #Находим по селектору поле ввода Postcode/ZIP
Postcode.send_keys("410080") #Вводим почтовый индекс
Postcode.click()
#Выберите способ оплаты "Check Payments". Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
driver.execute_script("window.scrollBy(0, 600);") #Проскролльте на 600 пикселей вниз
time.sleep(3) #Добавьте sleep
Check_pay = driver.find_element_by_css_selector("li.wc_payment_method.payment_method_cheque > label") #Выбираем способ оплаты "Check Payments"
Check_pay.click()
#Нажмите PLACE ORDER
Place_order_btn = driver.find_element_by_css_selector("#place_order") #Находим кнопку PLACE ORDER
Place_order_btn.click()
#Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
Thank_you = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
#Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
Check_Payments = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr:nth-child(3) > td"), "Check Payments"))
#Закрываем автотест
driver.quit()