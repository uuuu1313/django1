from datetime import date

def sayHello():
    return "hello"

def get_today():
    return date.today()

def function_to_get_today():
    day = get_today()
    return day