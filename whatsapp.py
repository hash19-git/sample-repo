import pywhatkit

try:
    pywhatkit.sendwhatmsg("+919944335320", "Hello from Hari", 13, 28)
    print("Successfully Sent!")
except ValueError as e:
    print("An Unexpected Error!",e)

NameError: