from optiflow.modules.client.models.client import Client

def get_client_by_id(compte):
    client = Client.query.filter_by(compte=compte).first()
    return client