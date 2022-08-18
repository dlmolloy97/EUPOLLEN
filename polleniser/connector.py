import cdsapi
import os
from dotenv import find_dotenv, load_dotenv
import rasterio
from rasterio.plot import reshape_as_raster, reshape_as_image

class CopernicusConnector:
    def __init__(self):
        print("Loading Data Store credentials")
        env_path = find_dotenv('.env')
        load_dotenv(env_path)
        print("Credentials configured")
    def query(self,json):
        c = cdsapi.Client(url=os.getenv('url'), key=os.getenv('key'))
        c.retrieve(
            'cams-europe-air-quality-forecasts',json,'./data/download.grib')

    def load_data(self):
        with rasterio.open('./data/download.grib') as src:
            raster = src.read()
            src.close()
        image = reshape_as_image(raster)
        return image
