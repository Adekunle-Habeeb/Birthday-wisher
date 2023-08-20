import smtplib

my_email = "bnaqeeliy@gmail.com"
password = "paymenter"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="adekunle22taiwo@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )



