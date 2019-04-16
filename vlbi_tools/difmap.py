import numpy as np
import pandas as pd
import astropy.units as u
from astropy.io import fits


def read_model(data_path):
    '''
    Read difmap model file in fits format and returns a pandas dataframe

    DATA_PATH: Path to difmap model in fits format
    '''
    difmap_data = fits.open(data_path)
    date = difmap_data['PRIMARY'].header['DATE-OBS']

    x_positions = difmap_data['AIPS CC'].data['DELTAX']
    y_positions = difmap_data['AIPS CC'].data['DELTAY']
    major_axes = difmap_data['AIPS CC'].data['MAJOR AX']
    minor_axes = difmap_data['AIPS CC'].data['MINOR AX']
    phi_ellipse = difmap_data['AIPS CC'].data['POSANGLE'] - 90
    flux = difmap_data['AIPS CC'].data['FLUX']

    # Shift Core to (0,0)
    x_positions_cor = x_positions - x_positions[0]  # in case first
    y_positions_cor = y_positions - y_positions[0]  # comp fits core!

    # Calculate radial distance
    radial_dist = np.sqrt(x_positions_cor**2 +
                          y_positions_cor**2)

    df_components = pd.DataFrame({'c_i': '',
                                  'date': date,
                                  'radial_dist': radial_dist,
                                  'flux': flux,
                                  'major_axes': major_axes,
                                  'minor_axes': minor_axes,
                                  'phi_ellipse': phi_ellipse,
                                  'x_positions': x_positions_cor,
                                  'y_positions': y_positions_cor,
                                  })

    return df_components






'''
minor_axes = (((difmap_data['AIPS CC'].data['MINOR AX'] *
                u.degree).to(u.mas)).value)
'''
