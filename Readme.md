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