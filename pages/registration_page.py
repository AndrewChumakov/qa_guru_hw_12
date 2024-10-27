import os

from selene import browser, have

CURRENT_FILE = os.path.abspath(__file__)
DIRECTORY = os.path.dirname(CURRENT_FILE)
FILE = os.path.join(DIRECTORY, "..", "resources")


class RegistrationPage:
    def open_page(self, page):
        browser.open(page)

    def remove_banner(self):
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def open_page_without_banners(self, page):
        self.open_page(page)
        self.remove_banner()

    def fill_first_name(self, first_name):
        browser.element("#firstName").type(first_name)

    def fill_last_name(self, last_name):
        browser.element("#lastName").type(last_name)

    def fill_email(self, email):
        browser.element("#userEmail").type(email)

    def set_gender(self, gender):
        browser.all("[name='gender']").element_by(have.attribute("value", gender)).element("../label").click()

    def fill_mobile(self, mobele_number):
        browser.element("#userNumber").type(mobele_number)

    def set_birth_date(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").click()
        browser.element(f"[value='{month}']").click()
        browser.element(".react-datepicker__year-select").click()
        browser.element(f"[value='{year}']").click()
        if len(day) == 2:
            browser.element(f".react-datepicker__day--0{day}").click()
        else:
            browser.element(f".react-datepicker__day--00{day}").click()

    def set_subject(self, subject):
        browser.element("#subjectsInput").type(subject[0].lower())
        browser.element(".subjects-auto-complete__menu-list").element(f"//*[text()='{subject}']").click()

    def set_hobby(self, hobby):
        browser.element(f"//label[text()='{hobby}']").click()

    def set_picture(self, file_name):
        browser.element("#uploadPicture").send_keys(os.path.abspath(f"{FILE}/{file_name}"))

    def fill_address(self, address):
        browser.element("#currentAddress").type(address)

    def fill_state(self, state):
        browser.element("#state").click()
        browser.element(f"//*[text()='{state}']").click()

    def fill_city(self, city):
        browser.element("#city").click()
        browser.element(f"//*[text()='{city}']").click()

    def submit(self):
        browser.element("#submit").click()

    def should_have_registered(self, name, email, gender, number, date_birth, subjects, hobbies, picture, address,
                               place):
        browser.element("//table//td[text()='Student Name']/../td[2]").should(have.exact_text(name))
        browser.element("//table//td[text()='Student Email']/../td[2]").should(have.exact_text(email))
        browser.element("//table//td[text()='Gender']/../td[2]").should(have.exact_text(gender))
        browser.element("//table//td[text()='Mobile']/../td[2]").should(have.exact_text(number))
        browser.element("//table//td[text()='Date of Birth']/../td[2]").should(have.exact_text(date_birth))
        browser.element("//table//td[text()='Subjects']/../td[2]").should(have.exact_text(subjects))
        browser.element("//table//td[text()='Hobbies']/../td[2]").should(have.exact_text(hobbies))
        browser.element("//table//td[text()='Picture']/../td[2]").should(have.exact_text(picture))
        browser.element("//table//td[text()='Address']/../td[2]").should(have.exact_text(address))
        browser.element("//table//td[text()='State and City']/../td[2]").should(have.exact_text(place))
