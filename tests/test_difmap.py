import numpy as np


def test_read_model():
    from vlbi_tools.difmap import read_model

    catalog = read_model('tests/resources/1638+118_model.fits')
    assert catalog.columns.tolist() == ['c_i', 'date', 'radial_dist', 'flux',
                                        'major_axes', 'minor_axes',
                                        'phi_ellipse', 'x_positions',
                                        'y_positions', 'noise_level']


def test_convert_model():
    from vlbi_tools.difmap import convert_model, read_model

    catalog = read_model('tests/resources/1638+118_model.fits')
    convert_model(catalog)

    assert np.all(np.abs(catalog['radial_dist'].values) <= 30)
