from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait

# === LOADING DATA ===

# Loading .env
load_dotenv()

# loading email OR usernames
userNames = os.getenv('USERNAMES')

# loading passwords
password = os.getenv("PASSWORD")

# Opening Chrome driver
driver = webdriver.Chrome()


# Opening the link to ERP
driver.get('https://erp2.ajku.edu.pk/')


# Running ERP for every user
for userName in userNames:
    # Finding email OR username textfield
    email_login = driver.find_element(By.ID, "email")
    # Filing the email OR username
    email_login.send_keys(userName)

    # Finding password textfield
    pass_input = driver.find_element(By.ID, "pass")
    # Filling the password
    pass_input.send_keys(password)

    # Finding usertype textfield
    userType_element = driver.find_element(By.ID,"user_type")

    # Filing userType as Student
    userType_element.send_keys("Student")

    # Finding usertype textfield
    dept_element = driver.find_element(By.ID, "dept")

    # Filing the field
    dept_element.send_keys("CS&IT Neelum Campus")

    # Finding login button
    form = driver.find_element(By.NAME, "form_login")

    # Logggin In
    form.submit()

    # Finding the Survey button
    survey_button = driver.find_element(By.LINK_TEXT, "Survey")

    # Click the survey button
    survey_button.click()



    # === COURSE SURVEY ===
    while True:


        # Fetching all books for survey
        course_survey = driver.find_elements(
            By.XPATH,
            '//a[contains(@href,"course_survey.php")]'
        )


        # If no book has survey remaining break the loop
        if len(course_survey) == 0:
            break

        # Doing survey of first book
        course_survey[0].click()


        # Filing all fields
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


        # Waiting for form to be submitted
        time.sleep(5)

        # Going back for another course survey
        driver.back()



    # ===   TEACHER SURVEY  ===
    while True:

        # Fetching alL teachers for survey
        teacher_survey = driver.find_elements(
                By.XPATH,
                '//a[contains(@href,"teacher_survey.php")]'
            )
        
        # If no teacher has survey remaining break the loop
        if len(teacher_survey) == 0:
            break

        # Doing survey of first teacher
        teacher_survey[0].click()
        
        # Filing all fields
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



        # Waiting for form to be submitted
        time.sleep(5)

        # Going back for another teacher survey
        driver.back()
    

    # Going to home page
    driver.back()

    # Going to login page
    driver.back()

    # Removing all filled fileds
    driver.refresh()



# Closing browser
driver.quit()

