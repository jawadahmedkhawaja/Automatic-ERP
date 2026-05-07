from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support.ui import WebDriverWait



# Opening Chrome driver
driver = webdriver.Chrome()

userNames = os.getenv('USERNAMES')
password = os.getenv("PASSWORD")
# Opening the link to ERP
driver.get('https://erp2.ajku.edu.pk/')



for userName in userNames:
    # Filling the Email (User Name By university)
    email_login = driver.find_element(By.ID, "email")
    email_login.send_keys(userName)

    pass_input = driver.find_element(By.ID, "pass")
    pass_input.send_keys(password)

    userType_element = driver.find_element(By.ID,"user_type")
    userType_element.send_keys("Student")

    dept_element = driver.find_element(By.ID, "dept")
    dept_element.send_keys("CS&IT Neelum Campus")

    form = driver.find_element(By.NAME, "form_login")
    form.submit()

    survey_button = driver.find_element(By.LINK_TEXT, "Survey")
    survey_button.click()



    # Course Survey

    while True:

        course_survey = driver.find_elements(
            By.XPATH,
            '//a[contains(@href,"course_survey.php")]'
        )

        if len(course_survey) == 0:
            break
        course_survey[0].click()

        driver.execute_script('''
        (function () {

            // ===== SETTINGS =====
            // Change this if you want different answers
            const defaultAnswer = "Strongly Agree";

            // ===== FILL RADIO BUTTONS =====
            document.querySelectorAll('input[type="radio"]').forEach(radio => {

                // Auto select "Strongly Agree"
                if (radio.value === defaultAnswer) {
                    radio.checked = true;
                }

                // Special cases
                if (radio.name === "ans-54" && radio.value === ">81%") {
                    radio.checked = true;
                }

                if (radio.name === "ans-87" && radio.value === "Full Time") {
                    radio.checked = true;
                }

                if (radio.name === "ans-88" && radio.value === "No") {
                    radio.checked = true;
                }

                if (radio.name === "ans-90" && radio.value === "Male") {
                    radio.checked = true;
                }

                if (radio.name === "ans-91" && radio.value === "22-29") {
                    radio.checked = true;
                }
            });

            // ===== FILL TEXT INPUTS =====
            const textInputs = document.querySelectorAll('input[type="text"]');

            const comments = [
                "Good course.",
                "Everything was well managed.",
                "Teaching method was effective.",
                "Resources were useful.",
                "Interesting subject.",
                "Assessment was fair.",
                "Instructor explained clearly.",
                "Tutorials were helpful.",
                "Practical work was useful.",
                "Very informative course.",
                "Could include more practical examples.",
                "Bagh"
            ];

            textInputs.forEach((input, index) => {
                input.value = comments[index] || "Good";
            });

            // ===== SUBMIT FORM =====
            setTimeout(() => {
                document.querySelector('#course_survey_submit').click();
                console.log("Survey submitted successfully.");
            }, 1000);

        })();
        ''')

        time.sleep(5)
        driver.back()



    # Teacher Survey
    while True:
        teacher_survey = driver.find_elements(
                By.XPATH,
                '//a[contains(@href,"teacher_survey.php")]'
            )

        if len(teacher_survey) == 0:
            break

        teacher_survey[0].click()
        

        driver.execute_script("""
                            (function () {

            // ===== SETTINGS =====
            const defaultAnswer = "Strongly Agree";

            // ===== AUTO ANSWER RADIO QUESTIONS =====
            document.querySelectorAll('input[type="radio"]').forEach(radio => {
                if (radio.value === defaultAnswer) {
                    radio.checked = true;
                }
            });

            // ===== COMMENTS =====
            const comments = [
                "Instructor explained concepts clearly and professionally.",
                "Course content was useful and well organized."
            ];

            // ===== FILL TEXT INPUTS =====
            const textInputs = document.querySelectorAll('input[type="text"]');

            textInputs.forEach((input, index) => {
                input.value = comments[index] || "Good";
            });

            // ===== SUBMIT FORM =====
            setTimeout(() => {
                document.querySelector('#teacher_survey_submit').click();
                console.log("Teacher survey submitted successfully.");
            }, 1000);

        })();

                            """)



        time.sleep(5)
        driver.back()
    
    driver.back()
    driver.back()
    driver.refresh()




driver.quit()

