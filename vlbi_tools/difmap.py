import numpy as np
import pandas as pd
from astropy.io import fits
from vlbi_tools.utils import deg2mas


def read_model(data_path):
    """
    Read difmap model file in fits format and returns a pandas dataframe

    DATA_PATH: Path to difmap model in fits format
    """
    difmap_data = fits.open(data_path)
    date = difmap_data['PRIMARY'].header['DATE-OBS']
    noise_level = difmap_data['PRIMARY'].header['NOISE']

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

    df_components = pd.DataFrame({
            'c_i': '',
            'date': date,
            'radial_dist': radial_dist,
            'flux': flux,
            'major_axes': major_axes,
            'minor_axes': minor_axes,
            'phi_ellipse': phi_ellipse,
            'x_positions': x_positions_cor,
            'y_positions': y_positions_cor,
            'noise_level': noise_level,
            })

    return df_components


def convert_model(dataframe):
    """
    Convert coordinates from difmap model to milliarcseconds

    DATAFRAME: Pandas dataframe of difmap model
    """
    df = dataframe

    df['radial_dist'] = deg2mas(df['radial_dist'].values)
    df['major_axes'] = deg2mas(df['major_axes'].values)
    df['minor_axes'] = deg2mas(df['minor_axes'].values)
    df['x_positions'] = deg2mas(df['x_positions'].values)
    df['y_positions'] = deg2mas(df['y_positions'].values)
