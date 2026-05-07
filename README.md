<h1 align="center" style="font-size:40px;">Disclaimer</h1>

<p align="center" style="font-size:20px;">This tool is intended for educational purposes to demonstrate web automation. Use it responsibly and in accordance with your institution's policies. Automated survey completion may violate academic integrity guidelines. The authors are not responsible for any misuse or consequences.</p>

---

# ERP Survey Automation

## Overview

This project automates the tedious process of filling out ERP surveys for semester courses and teachers at **UAJ&K (University of Azad Jammu & Kashmir)**. The manual process involves filling out 30-40 options per subject for both course and teacher surveys, which becomes extremely tiring with 6-7 subjects per semester. This Selenium-based automation script streamlines the entire process by automatically logging in, navigating to surveys, and completing them with predefined responses.

## Features

- **Multi-User Support**: Automates surveys for multiple student accounts using credentials stored in a `.env` file.
- **Course Survey Automation**: Automatically fills out course evaluation forms with consistent, positive responses.
- **Teacher Survey Automation**: Handles teacher evaluation surveys with appropriate feedback.
- **Customizable Responses**: Easily modify default answers and comments in the script.
- **Error Handling**: Includes waits and navigation to handle page loads and submissions.
- **Chrome Driver Integration**: Uses Selenium WebDriver for browser automation.

## Prerequisites

- Python 3.x installed on your system.
- Google Chrome browser.
- ChromeDriver (automatically managed by Selenium, but ensure compatibility with your Chrome version).
- A `.env` file containing your ERP login credentials.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jawadahmedkh/Automatic-ERP-UAJK.git   
   cd Automatic-ERP-UAJK
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv seleniumVenv
   seleniumVenv\Scripts\activate  # On Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your ERP credentials:
     ```
     USERNAMES=your_username1,your_username2,your_username3  # Comma-separated list of usernames/emails
     PASSWORD=your_password
     ```
   - **Security Note**: Never commit the `.env` file to version control. Add it to `.gitignore`.

## Usage

1. Ensure your `.env` file is properly configured with valid credentials.
2. Run the automation script:
   ```bash
   python main.py
   ```
3. The script will:
   - Open Chrome and navigate to the ERP login page.
   - Log in for each user in the list.
   - Complete all pending course surveys.
   - Complete all pending teacher surveys.
   - Move to the next user until all surveys are done.
4. Monitor the console for progress updates.

## Configuration

### Default Answers
The script uses "Strongly Agree" as the default answer for radio button questions. You can modify this in the JavaScript sections within `main.py`:

```python
const defaultAnswer = "Strongly Agree";
```

### Special Cases
Certain questions have hardcoded responses (e.g., attendance percentage, employment status). Edit these in the script if needed:

- Attendance: ">81%"
- Employment: "Full Time"
- Additional questions: "No", "Male", "22-29"

### Comments
Predefined comments are used for text inputs. Customize the `comments` array in the script:

```python
const comments = [
    "Good course.",
    "Everything was well managed.",
    // ... add more
];
```

## How It Works

1. **Login Loop**: Iterates through each username in the `.env` file.
2. **Navigation**: Logs in and clicks the "Survey" button.
3. **Course Surveys**: Finds and clicks course survey links, fills forms using JavaScript injection, submits, and navigates back.
4. **Teacher Surveys**: Similar process for teacher evaluations.
5. **Completion**: Continues until no surveys remain for the current user, then proceeds to the next.

## Troubleshooting

- **ChromeDriver Issues**: Ensure ChromeDriver matches your Chrome version. Selenium Manager handles this automatically in newer versions.
- **Login Failures**: Verify credentials in `.env` and check for CAPTCHA or additional security measures.
- **Survey Not Found**: Ensure surveys are available for the logged-in user.
- **Timeouts**: Adjust `time.sleep()` values if pages load slowly.



## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.