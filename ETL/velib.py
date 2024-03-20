# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=wildcard-import
# pylint: disable=W0614
import configparser
import requests
import pandas as pd
from azure_configuration import AzureConfiguration
from azure.storage.blob import BlobServiceClient


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

	list_dfs=[]

	for name, url in urls:
    	# Data extraction
    	extractor_instance = extractor(url)
    	data = extractor_instance.extract_data()
    	#print(data)

    	# Data transformation
    	transformer_instance = transformer(extractor_instance)
    	df = transformer_instance.create_dataframe()
    	print(df)

    	list_dfs.append(df)

	# Dataframe concatanation using station_id as join key

	concatenated_df=pd.concat(list_dfs,ignore_index=True)
	print(concatenated_df)

    config = configparser.ConfigParser()
    config.read('config.ini')
    azure_storage_connection_string = config['Azure']['storage_connection_string']
    container_name = config['Azure']['container_name']
    blob_name = config['Azure']['blob_name']

	# Create an instance of azure_config
	azure_config = AzureConfiguration(
    	azure_storage_connection_string=azure_storage_connection_string,
    	container_name=container_name,
    	blob_name=blob_name
	)

	# Push dataframe concata
	azure_config.push_dataframe_to_blob(concatenated_df)
