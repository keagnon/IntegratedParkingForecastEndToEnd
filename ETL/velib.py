# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=wildcard-import
# pylint: disable=W0614

import requests
import pandas as pd


class extractor():

    """ Goal : Extract data from velib API"""

    def __init__(self,url):
       self.url=url

    def extract_data(self):
        """ Extract data from API"""
        response=requests.get(self.url)
        data=response.json()
        return data

class transformer():

    """ Goal : Transform data extracted"""

    def __init__(self,extractor):
        self.extractor=extractor

    def create_dataframe(self):
        """ Create dataframe base on data collected """
        stations_info=self.extractor.extract_data()
        stations_info=stations_info["data"]["stations"]
        df=pd.DataFrame(stations_info)
        return df

if __name__=='__main__':

    urls = [
        ("station_info", "https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_information.json"),
        ("station_status", "https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_status.json")
    ]

    for name, url in urls:
        # Extraction des données
        extractor_instance = extractor(url)
        data = extractor_instance.extract_data()
        print(data)

        # Transformation des données
        transformer_instance = transformer(extractor_instance)
        df = transformer_instance.create_dataframe()
        print(df)
