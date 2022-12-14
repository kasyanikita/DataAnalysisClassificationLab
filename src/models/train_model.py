# -*- coding: utf-8 -*-
import click
import logging
import pandas as pd
from pathlib import Path
from train import train_model, save_model, save_labels
from dotenv import find_dotenv, load_dotenv


@click.command()
@click.argument('input_data_filepath', type=click.Path(exists=True))
@click.argument('input_target_filepath', type=click.Path(exists=True))
@click.argument('output_model_filepath', type=click.Path())
@click.argument('output_val_folderpath', type=click.Path())
def main(input_data_filepath, input_target_filepath, output_model_filepath, output_val_folderpath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    
    train = pd.read_pickle(input_data_filepath)
    target = pd.read_pickle(input_target_filepath)
    model, val_true, val_pred = train_model(train, target)
    save_labels(val_true, val_pred, output_val_folderpath)
    save_model(model, output_model_filepath)
    
    


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()