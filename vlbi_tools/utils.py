import astropy.units as u


def deg2mas(value):
    '''
    Converts value from degree to milliarcseconds

    value: a value in degree
    '''
    value_mas = (value * u.degree).to(u.mas).value
    return value_mas
