import smtplib

print("starting..")
fromaddr = 'vtran40@gatech.edu'
toaddr = 'daivinhtran.vt@gmail.com'

msg = 'vinh'

print("configuring smtp...")
server = smtplib.SMTP("smtp.office365.com", 587)


print("start tls...")
server.starttls()

print("login...")
server.login('vtran40', 'Big_Dream1994')

print("sending email...")
server.sendmail(fromaddr, toaddr, msg)


server.quit()