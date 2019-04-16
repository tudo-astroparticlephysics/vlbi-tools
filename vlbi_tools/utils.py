import numpy as np
import astropy.units as u
import pandas as pd


def deg2mas(value):
    '''
    Converts value from degree to milliarcseconds

    value: a value in degree
    '''
    value_mas = (value * u.degree).to(u.mas).value

    return value_mas


def time_diff(catalog):
    """
    Calculates the time difference between differen epochs and adds it to the
    component catalog

    CATALOG: Component catalog with different observation epochs
    """
    dates = (pd.to_datetime(catalog['date'], format='%Y-%m-%d'))
    delta_days = ((dates - dates.min()) / np.timedelta64(1, 'D'))
    delta_days = pd.DataFrame({'delta_days': delta_days})
    catalog = pd.concat([catalog, delta_days], axis=1)

    return catalog
