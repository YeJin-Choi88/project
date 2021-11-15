import serial

arduino = serial.Serial('COM3', 9600)

import pyotp
totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
print("Current OTP:", totp.now())

a = pyotp.totp.TOTP('JBSWY3DPEHPK3PXP').provisioning_uri(name='yejin@google.com', issuer_name='Secure App')
b = pyotp.hotp.HOTP('JBSWY3DPEHPK3PXP').provisioning_uri(name="yejin@google.com", issuer_name="Secure App", initial_count=0)


print('serial ' + serial.__version__)

# Set a PORT Number & baud rate
PORT = 'COM4'
BaudRate = 9600

ARD= serial.Serial(PORT,BaudRate)

A=1234

A=str(A)
Trans="Q" + A
Trans= Trans.encode('utf-8')


while(True):

    c=arduino.readline()

    c = c.decode()

    if(len(c)>=6):
        print(c)
        break
password = int(c.strip())
otp = int(totp.now())



while(True):
    if(password == otp):
        ARD.write(Trans)
        
    else:
        break
