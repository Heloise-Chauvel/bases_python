from google.cloud import secretmanager

client = secretmanager.SecretManagerServiceClient()

def get_secret(secret_id: str, version: str = "latest") -> str:
    project_id="exelcia-heloise"
    name= f"projects/{project_id}/secrets/{secret_id}/versions/{version}"
    try:
        response = client.access_secret_version(request={"name":name})
        return response.payload.data.decode("UTF-8")
    except Exception as e:
        raise RuntimeError(f"Error accessing secret {secret_id}:{e}")