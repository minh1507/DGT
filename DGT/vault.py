import hvac
import os

def get_vault_client():
    VAULT_URL = "http://222.255.1.152:1502"
    VAULT_TOKEN = "hvs.FAObWeU22Fxvg4QfA9X5eSGZ"
    
    client = hvac.Client(url=VAULT_URL, token=VAULT_TOKEN)

    if not client.is_authenticated():
        raise Exception("Vault authentication failed!")

    return client

def load_vault_secrets_to_env():
    client = get_vault_client()
    secrets = client.secrets.kv.v2.read_secret_version(path='DGT/dgt_dev')
    
    for key, value in secrets['data']['data'].items():
        os.environ[key] = value