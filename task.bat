@echo on

schtasks /create /tn "pic_mail" /tr "python sendmail.with_pic.py" /sc HOURLY /mo 2 /st 08:00 /et 22:00 /ru "system"

pause