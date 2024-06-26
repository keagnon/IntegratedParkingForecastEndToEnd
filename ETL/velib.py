# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=wildcard-import
# pylint: disable=W0614
import os
import requests
import pandas as pd
from azure_configuration import AzureConfiguration
from azure.storage.blob import BlobServiceClient


class Extractor:
    """Goal : Extract data from velib API"""

    def __init__(self, url):
        self.url = url

    def extract_data(self):
        """Extract data from API"""
        response = requests.get(self.url)
        data = response.json()
        return data


class Transformer:
    """Goal : Transform data extracted"""

    def __init__(self, extractor):
        self.extractor = extractor

    def create_dataframe(self):
        """Create dataframe base on data collected """
        stations_info = self.extractor.extract_data()
        stations_info = stations_info["data"]["stations"]
        df = pd.DataFrame(stations_info)
        return df


if __name__ == '__main__':

    urls = [
        ("station_info", "https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_information.json"),
        ("station_status", "https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_status.json")
    ]

    list_dfs = []

    for name, url in urls:
        # Data extraction
        extractor_instance = Extractor(url)
        data = extractor_instance.extract_data()
        # print(data)

        # Data transformation
        transformer_instance = Transformer(extractor_instance)
        df = transformer_instance.create_dataframe()
        print(df)

        list_dfs.append(df)

    # Dataframe concatenation using station_id as join key

    concatenated_df = pd.concat(list_dfs, ignore_index=True)
    print(concatenated_df)

    azure_storage_connection_string = os.environ.get('STORAGE_CONNECTION_STRING')
    container_name = "rncpprojectcontainer"
    blob_name = "velib_data_extract"

    # Create an instance of azure_config
    azure_config = AzureConfiguration(
        azure_storage_connection_string=azure_storage_connection_string,
        container_name=container_name,
        blob_name=blob_name
    )

    # Push dataframe concatenation
    azure_config.load_dataframe(concatenated_df)
