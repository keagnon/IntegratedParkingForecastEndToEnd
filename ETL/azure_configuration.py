from azure.storage.blob import BlobServiceClient
from io import StringIO

class AzureConfiguration:

    def __init__(self, azure_storage_connection_string, container_name, blob_name):
        self.azure_storage_connection_string = azure_storage_connection_string
        self.container_name = container_name
        self.blob_name = blob_name
        self.blob_service_client = BlobServiceClient.from_connection_string(azure_storage_connection_string)

    def push_dataframe_to_blob(self, dataframe):
        file_name = f"{self.blob_name}.csv"

        # Convertir le DataFrame au format CSV
        csv_data = dataframe.to_csv(index=False)

        # Convertir les données CSV en bytes
        data_bytes = csv_data.encode('utf-8')

        # Envoyer les données au blob
        blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=file_name)
        blob_client.upload_blob(data_bytes, overwrite=True)

        print(f"Dataframe envoyé avec succès à Azure Blob Storage : {file_name}")
