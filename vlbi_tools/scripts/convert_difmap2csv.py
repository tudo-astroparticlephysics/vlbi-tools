import click
import os
import glob
import pandas as pd
from vlbi_tools import difmap
from vlbi_tools.utils import time_diff


@click.command()
@click.argument('data_path', type=click.Path(exists=True, dir_okay=True))
@click.argument('model_name')
@click.argument('out_path', type=click.Path(exists=False, dir_okay=True))
def main(data_path, model_name, out_path):
    '''
    Converts difmap models in fits format into csv catalog. Searches for model
    files from a top level directory and summarizes all information in one
    file.

    DATA_PATH: path to top level directory of difmap models
    MODEL_NAME: Name of the difmap model, all model files need to have the same
                name
    OUT_PATH: path to directory to save catalog
    '''
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    data_paths = sorted(glob.glob(data_path+'/*/'+model_name+'.fits'))

    catalog = pd.DataFrame()

    for path in data_paths:
        model = difmap.read_model(path)
        catalog = pd.concat([catalog, model], ignore_index=True)

    difmap.convert_model(catalog)
    catalog = time_diff(catalog)

    catalog.to_csv(out_path + '/catalog.csv')


if __name__ == '__main__':
    main()
