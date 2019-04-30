# Created by Alexander Watzinger and others. Please see README.md for licensing information


def uc_first(string):
    return str(string)[0].upper() + str(string)[1:] if string else ''
