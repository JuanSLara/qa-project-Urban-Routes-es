from faulthandler import is_enabled

from selenium.webdriver.chrome.service import Service
from data.data import card_number
from data.data import card_code
from pages import urban_routes_page as urp
from data import data
from selenium import webdriver




class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = urp.UrbanRoutesPage(cls.driver)

#Primer test, envia las direcciones desde-hasta y verifica que sean correctas
    def test_1_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)

        #compara el resultado actual y el esperado
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to


#Segundo test, ckick en pedir un taxi y seleccionar tarifa confort
    def test_2_select_confort(self):
        self.routes_page.select_taxi()
        self.routes_page.select_comfort()
        assert self.routes_page.is_comfort_selected(), "El botón Comfort no se seleccionó correctamente"


#Tercer test, rellenar el numero de telefono
    def test_3_set_number_phone(self):
        self.routes_page.add_phone()
        assert self.routes_page.get_number_phone() == data.phone_number


#Cuarto test, Agregar una tarjeta de
    def test_4_payment_method(self):

        self.routes_page.select_payment()
        self.routes_page.send_numbers_card()
        self.routes_page.finish_add_payment()
        assert self.routes_page.get_card_number() == data.card_number
        assert self.routes_page.get_card_code() == data.card_code
        self.routes_page.button_x()


#Quinto test, Escribir un mensaje para el conductor.
    def test_5_msm_driving(self):
        self.routes_page.set_sms_driving(data.message_for_driver)
        assert self.routes_page.get_sms_driving() == data.message_for_driver


#Sexto test, Pedir una manta y pañuelos.
    def test_6_blankets_and_scarves(self):
        self.routes_page.set_blanket()
        assert self.routes_page.get_checkbox_blanket(), 'manta y pañuelos no ha sido seleccionado'
        #assert self.page.is_blanket_and_tissues_selected(), "La opción de manta y pañuelos no fue activada"


#Septimo test, Pedir 2 helados
    def test_7_add_ice_cream(self):
        self.routes_page.add_ice_cream()
        assert self.routes_page.get_ice_cream_counter() == 2, 'no se agregaron dos helados'


#Octavo test, Aparece el modal para buscar un taxi.
    def test_8_visible_modal(self):
        self.routes_page.click_reserve_button()
        assert self.routes_page.visible_reserve_modal(), 'no se muestra modal de buscar taxi'


#Noveno test, aparece la información del conductor
    def test_9_visible_info_driver(self):
        img_drive = self.routes_page.visible_driver_information()
        assert img_drive, 'Imagen del conductor no es visible'


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()