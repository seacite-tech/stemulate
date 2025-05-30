import os
import time
from dotenv import load_dotenv
from smtp import send_email_with_html

# Load environment variables
load_dotenv()

# Configuration from environment variables
CONFIG = {
    "SENDER_EMAIL": os.getenv("SENDER_EMAIL"),
    "APP_PASSWORD": os.getenv("APP_PASSWORD"),
    "EMAIL_SUBJECT": os.getenv("EMAIL_SUBJECT", "STEMulate is back!"),
    "THROTTLE_SECONDS": int(os.getenv("THROTTLE_SECONDS", 10)),
}

# Validate required configuration
for key in ["SENDER_EMAIL", "APP_PASSWORD"]:
    if not CONFIG[key]:
        raise ValueError(f"Missing required environment variable: {key}")

def generate_email_content() -> str:
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>STEMulate is back!</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        /* Basic Reset & Body Styles */
        body {{
            margin: 0;
            padding: 0;
            background-color: #f4f4f4 !important; /* Light grey background for email client compatibility */
            color: #333333 !important; /* Darker text for readability */
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
            line-height: 1.6;
        }}

        /* Table and Container Styles */
        .email-container {{
            max-width: 600px;
            margin: 20px auto;
            background-color: #ffffff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Softer, more prominent shadow */
            -webkit-font-smoothing: antialiased;
        }}

        .header-section {{
            background-color: #DB0C0C; /* Dark Red */
            padding: 25px 30px;
            text-align: left;
            color: #ffffff; /* White text for header */
        }}

        .content-section {{
            padding: 30px; /* This padding gives space from the white box edges */
            color: #333333;
        }}

        .footer-section {{
            background-color: #f0f0f0; /* Light grey footer */
            padding: 20px 30px;
            text-align: center;
            font-size: 12px;
            color: #777777;
        }}

        /* Image Styles */
        .logo {{
            max-width: 180px; /* Slightly larger logo */
            height: auto;
            display: block;
            margin: 0; /* Remove all margins to hug the corner of its container */
            padding-bottom: 10px; /* Add some space below the logo */
        }}

        /* Text Styles */
        h2, h3 {{
            color: #DB0C0C; /* Red headings for emphasis */
            margin-top: 1.5em;
            margin-bottom: 0.8em;
            font-weight: 600;
        }}

        p {{
            margin: 0 0 1em 0;
        }}

        .date {{
            text-align: right;
            font-size: 14px;
            color: #555555;
            margin-bottom: 20px;
        }}

        .recipient {{
            text-align: left;
            font-size: 14px;
            color: #555555;
            margin-bottom: 20px;
        }}

        .signature {{
            margin-top: 30px;
            font-weight: 600; /* Slightly bolder */
            color: #333333;
        }}

        a {{
            color: #DB0C0C; /* Link color */
            text-decoration: none; /* No underline by default */
        }}

        a:hover {{
            text-decoration: underline; /* Underline on hover for links */
        }}

        ul {{
            list-style-type: disc;
            padding-left: 20px;
            margin-bottom: 1em;
        }}

        li {{
            margin-bottom: 0.5em;
        }}

        /* Responsive Styles */
        @media only screen and (max-width: 600px) {{
            .email-container {{
                width: 100% !important;
                margin: 0 auto !important;
                border-radius: 0;
            }}
            .content-section {{
                padding: 20px !important;
            }}
            .header-section {{
                padding: 20px !important;
            }}
            .logo {{
                max-width: 150px;
            }}
        }}
    </style>
</head>
<body>
<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
        <tr>
            <td align="center">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="600" class="email-container">
                    <tr>
                        <td class="header-section">
                            </td>
                    </tr>
                    <tr>
                        <td class="content-section">
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                <tr>
                                    <td style="text-align: left; padding-bottom: 15px;">
                                        <img src="https://stemulateprogram.com/logo2.png" width="140" alt="STEMulate Logo" class="logo">
                                    </td>
                                </tr>
                                <tr>
                                    <td style="text-align: right;">
                                        <p class="date">May 27, 2025</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <h3>STEMulate is back!</h3>
                                        <p>STEMulate is a virtual program where students will immerse themselves in the world of academic research. They'll learn to develop compelling research questions, effectively analyze data, and ultimately work towards writing a comprehensive research paper, all under the <b>one-on-one guidance of experienced mentors</b>.</p>
                                        <p>Beyond individualized mentorship, participants will engage in interactive workshops covering critical aspects of research, including methodology, ethics, and advanced writing skills. The program culminates in a <b>virtual symposium</b> where students proudly present their completed work to peers and experts.</p>
                                        <p>Our dedicated mentors hail from prestigious institutions such as <b>Georgetown University, UC Berkeley, Stanford University, Princeton University, Purdue University, and Utah State University</b>, bringing a wealth of knowledge across both STEM and social science disciplines.</p>

                                        <p>Explore diverse themes for your research:</p>
                                        <ul>
                                            <li>Biology, Chemistry, Physics, Psychology, Neuroscience</li>
                                            <li>Mathematics, Engineering, Computer Science, Economics</li>
                                            <li>Sociology, Political Science, History, Gender Studies</li>
                                            <li>Ecology, Media Studies, Education, and Business</li>
                                        </ul>
                                        <h3>Program Details:</h3>
                                        <p><strong>Language</strong>: English</p>
                                        <p><strong>Format</strong>: Exclusively online via Zoom.</p>
                                        <p><strong>Priority Application Deadline</strong>: June 16th at 11:59 PM (UTC-5)</p>
                                        <p><strong>Final Application Deadline</strong>: June 23th at 11:59 PM (UTC-5)</p>
                                        <p><strong>Application Portal</strong>: <a href="https://stemulateprogram.com/apply">https://stemulateprogram.com/apply</a>.</p>
                                        <hr />

                                        <p>You can find more details and information on our website: <a href="https://stemulateprogram.com" target="_blank">https://www.stemulateprogram.com</a>.</p>

                                        <p>Should you have any questions, please don't hesitate to reach out to us at <a href="mailto:stemulate.program@gmail.com" style="color: #DB0C0C; text-decoration: none;">stemulate.program@gmail.com</a>.</p>

                                        <p class="signature">Best regards, <br>STEMulate Admissions Team</p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td class="footer-section">
                            <p>&copy; 2025 STEMulate Program. All rights reserved.</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
"""

def load_recipient_list() -> list:
    """Load and validate recipient emails."""
    return [
        email.strip() for email in
        ["test@gmail.com"] # list of emails can be extended or loaded from a file
        if '@' in email
    ]

def main():
    """Main execution flow."""
    recipients = load_recipient_list()

    for email in recipients:
        try:
            print(f"Sending to {email}")
            html_content = generate_email_content()
            send_email_with_html(CONFIG["SENDER_EMAIL"], CONFIG["APP_PASSWORD"], email, CONFIG["EMAIL_SUBJECT"], html_content)
            time.sleep(CONFIG["THROTTLE_SECONDS"])
        except Exception as e:
            print(f"Failed to process {email}: {str(e)}")

if __name__ == "__main__":
    main()
