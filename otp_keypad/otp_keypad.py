import serial
import ex

arduino = serial.Serial('COM3', 9600)

import pyotp
totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
print("Current OTP:", totp.now())

a = pyotp.totp.TOTP('JBSWY3DPEHPK3PXP').provisioning_uri(name='yejin@google.com', issuer_name='Secure App')
b = pyotp.hotp.HOTP('JBSWY3DPEHPK3PXP').provisioning_uri(name="yejin@google.com", issuer_name="Secure App", initial_count=0)

while(True):

    c=arduino.readline()

    c = c.decode()

    if(len(c)>=6):
        print(c)
        break
password = int(c.strip())
otp = int(totp.now())
if(password == otp):
    print("열렸습니다")
else:
    print(otp)
    print("닫혔습니다.")