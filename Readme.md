Project:
Demonstrates how to create a bottle web application to control the
onion omega GPIO.

Setup Notes
vi /etc/opkg.conf
— delete line ‘option check_signature 1'
opkg update
wget --no-check-certificate https://github.com/defnull/bottle/raw/master/bottle.py
opkg install python-light
opkg install python-email
opkg install python-codecs
opkg install python-logging
opkg install python-openssl
opkg install openssh-sftp-server


Source Code:
https://github.com/youngsoul/OmegaGPIO


Credits:
From user Dan L
https://community.onion.io/topic/40/simple-python-wrapper-and-demo

Dan L - wrote the initial implementation of the GPIOHelper.  As Isaac Newton
once said, "If I have seen further, it is by standing on the shoulders of giants"

Thanks Dan L for the initial implementation.
