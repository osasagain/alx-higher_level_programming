#!/usr/bin/python3
def safe_print_division(a, b):
    res = 0
    try:
        res = a / b
    except Exception:
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res#!/usr/bin/python3
def safe_print_division(a, b):
    res = 0
    try:
        res = a / b
    except Exception:
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res
