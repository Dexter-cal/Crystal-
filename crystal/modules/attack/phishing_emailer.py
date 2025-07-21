import smtplib

def launch_phishing_email(target):
    print(f"[*] Launching phishing email to {target}...")
    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login("user@example.com", "password")
        message = "Subject: Urgent Security Alert\n\nThis is a test phishing email."
        server.sendmail("user@example.com", target, message)
        server.quit()
        print("[+] Phishing email sent successfully.")
    except Exception as e:
        print(f"[-] Failed to send phishing email: {e}")
