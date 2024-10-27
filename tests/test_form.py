import allure

from pages.registration_page import RegistrationPage


@allure.label("owner", "achumakov")
@allure.feature("Регистрация пользователя")
@allure.story("Пользователь успешно регистрируется")
def test_fill_form(browser_driver):
    with allure.step("Зарегистрировать пользователя"):
        registration_page = RegistrationPage()
        registration_page.open_page_without_banners("/automation-practice-form")
        registration_page.fill_first_name("First")
        registration_page.fill_last_name("Last")
        registration_page.fill_email("qwerty@test.ru")
        registration_page.set_gender("Female")
        registration_page.fill_mobile("4567891230")
        registration_page.set_birth_date("1990", "6", "14")
        registration_page.set_subject("Hindi")
        registration_page.set_subject("Maths")
        registration_page.set_hobby("Reading")
        registration_page.set_picture("picture.png")
        registration_page.fill_address("Any address")
        registration_page.fill_state("NCR")
        registration_page.fill_city("Gurgaon")
        registration_page.submit()
    with allure.step("Проверить регистрацию"):
        registration_page.should_have_registered("First Last",
                                                 "qwerty@test.ru",
                                                 "Female",
                                                 "4567891230",
                                                 "14 July,1990",
                                                 "Hindi, Maths",
                                                 "Reading",
                                                 "picture.png",
                                                 "Any address",
                                                 "NCR Gurgaon")
