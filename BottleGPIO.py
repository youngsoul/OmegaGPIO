from bottle import route, run, template
from GPIOHelper import GPIOHelper


@route('/gpio/<pin:int>/<value:int>')
def set_gpio(pin,value):
    gpio = GPIOHelper()
    gpio.setPin(pin,value)
    return template("Set pin={{pin}}, to value={{value}}", pin=pin, value=value)

@route('/gpio/<pin:int>')
def get_gpio(pin):
    gpio = GPIOHelper()
    pin_value = gpio.getPin(pin)
    return template("Get pin={{pin}}, is value={{value}}", pin=pin, value=pin_value)


run(host='0.0.0.0', port="8080", debug=True, reloader=True)
