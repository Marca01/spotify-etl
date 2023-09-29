from .Extract import return_dataframe
from .Transform import data_quality, transform_df
from .Load import upload

def spotify_etl():
    extracted_data = return_dataframe()

    data_quality(extracted_data)
    transformed_data = transform_df(extracted_data)

    upload(transformed_data)