from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import data
from utils.retrive_code import retrieve_phone_code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_rate = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Comfort']]")
    number_field = (By.CSS_SELECTOR, '.np-text')
    number_ph = (By.ID, 'phone')
    next_button = (By.CSS_SELECTOR, ".button.full")
    sms_field = (By.ID, 'code')
    confirm_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    payment_button = (By.CSS_SELECTOR, '.pp-button.filled')
    add_card = (By.CSS_SELECTOR, '.pp-row.disabled')
    card_number_field = (By.ID, 'number')
    cvv_code = (By.XPATH, '//*[@id="code" and @placeholder="12"]')
    add_button = (By.XPATH, '//button[text()="Agregar"]')
    card_page = (By.CLASS_NAME, 'card-wrapper')
    x_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    driving_message = (By.ID, 'comment')
    blanket_button = (By.CSS_SELECTOR, '.reqs-body > div:nth-child(1) > div > div.r-sw > div > span')
    checkbox = (By.CSS_SELECTOR, 'input.switch-input')
    ice_cream_button = (By.CSS_SELECTOR, '.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus')
    ice_cream_counter =  (By.CSS_SELECTOR, '.counter-value')
    reserve_button = (By.CSS_SELECTOR, '.smart-button-wrapper > button')
    visible_modal = (By.CSS_SELECTOR, '.order.shown > div.order-body')
    visible_driver = (By.CSS_SELECTOR, '.order-body')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.card_number_field = (By.ID, 'number')

    #Envio de direccion a los campos desde y hasta
    def set_from(self, from_address):
        self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(EC.presence_of_element_located(self.to_field)).send_keys(to_address)

#obtiene el valor que tiene el campo desde
    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

#obtiene el valor que tiene el campo hasta
    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

#Envia las dos direcciones
    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

#Buscar elemento para pedir taxi y hacer click en el
    def get_button_taxi(self):
        return self.wait.until(EC.element_to_be_clickable(self.order_taxi_button))

    def click_button_taxi(self):
        self.get_button_taxi().click()

#Selecciona el taxi
    def select_taxi(self):
        self.get_button_taxi()
        self.click_button_taxi()

#Buscar la tarifa Comfort y hacer click
    def get_comfort(self):
       return self.wait.until(EC.element_to_be_clickable(self.comfort_rate))

    def click_comfort(self):
        self.get_comfort().click()

#Selecciona Comfort
    def select_comfort(self):
        self.get_comfort()
        self.click_comfort()

    def is_comfort_selected(self):
        return "active" in self.get_comfort().get_attribute("class")

#Busca y Selecciona el campo numero
    def get_number(self):
        return self.wait.until(EC.element_to_be_clickable(self.number_field)).click()

 #Busca, llena el numero de telefono y obtener su valor
    def set_number_phone(self, phone_number):
        self.wait.until(EC.element_to_be_clickable(self.number_ph)).send_keys(data.phone_number)

    def get_number_phone(self):
        return self.driver.find_element(*self.number_ph).get_property('value')

#buscar y click en boton siguiente
    def click_next_button(self):
        self.wait.until(EC.element_to_be_clickable(self.next_button)).click()

#buscar el campo y envia el codigo sms
    def set_sms(self):
        code = retrieve_phone_code(self.driver)
        self.wait.until(EC.element_to_be_clickable(self.sms_field)).send_keys(code)

#Buscar elemento "boton confirmar" y darle click
    def get_confirm_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.confirm_button))

    def click_confirm_button(self):
        self.get_confirm_button().click()

#Metodo para agregar telefono
    def add_phone(self):
        self.get_number()
        self.set_number_phone(data.phone_number)
        self.click_next_button()
        self.set_sms()
        self.click_confirm_button()

#Buscar y hacer click en boton metodo de pago y agregar tarjeta
    def click_payment_method(self):
        self.wait.until(EC.visibility_of_element_located(self.payment_button)).click()

    def click_add_card(self):
        self.wait.until(EC.element_to_be_clickable(self.add_card)).click()

    def select_payment(self):
        self.click_payment_method()
        self.click_add_card()

#Envio de numeros a los campos numero tarjeta y codigo CCV
    def set_card_number(self, card_number):
        self.wait.until(EC.element_to_be_clickable(self.card_number_field)).send_keys(card_number)

    def get_card_number(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')

    def set_card_code(self, card_code):
        self.wait.until(EC.element_to_be_clickable(self.cvv_code)).send_keys(card_code)

    def get_card_code(self):
        return self.driver.find_element(*self.cvv_code).get_property('value')

#Envio de los dos campos (numero y tarjeta)
    def send_numbers_card(self):
        self.set_card_number(data.card_number)
        self.set_card_code(data.card_code)

#click en boton agregar y boton x
    def click_page(self):
        self.wait.until(EC.presence_of_element_located(self.card_page)).click()

    def click_add_button(self):
        self.wait.until(EC.element_to_be_clickable(self.add_button)).click()

    def button_x(self):
        self.wait.until(EC.element_to_be_clickable(self.x_button)).click()


#Finalizar proceso de tarjeta
    def finish_add_payment(self):
        self.click_page()
        self.click_add_button()


#Buscar el campo para enviar mensaje al conductor y enviar mensaje
    def set_sms_driving(self, message):
        self.wait.until(EC.element_to_be_clickable(self.driving_message)).send_keys(message)

    def get_sms_driving(self):
        return self.driver.find_element(*self.driving_message).get_property('value')

#Buscar elementos Pedir una manta y pañuelos y dar click
    def set_blanket(self):
        element = self.wait.until(EC.element_to_be_clickable(self.blanket_button))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def get_checkbox_blanket(self):
        check_box = self.driver.find_element(*self.checkbox)
        return check_box.is_selected()


#Buscar contador y boton para agregar helado
    def  add_ice_cream(self):
        button_add = self.wait.until(EC.element_to_be_clickable(self.ice_cream_button))
        self.driver.execute_script("arguments[0].scrollIntoView();", button_add)
        button_add.click()
        button_add.click()

    def get_ice_cream_counter(self):
        counter = self.driver.find_element(*self.ice_cream_counter)
        return int(counter.text)


#Modal para buscar taxi aparece en pantalla
    def click_reserve_button(self):
         self.wait.until(EC.element_to_be_clickable(self.reserve_button)).click()

    def visible_reserve_modal(self):
        img_modal = self.wait.until(EC.element_to_be_clickable(self.visible_modal))
        return img_modal.is_displayed()

#Informacion del condutor
    def visible_driver_information(self):
        img_driver = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.visible_driver))
        return img_driver.is_displayed()























