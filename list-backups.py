from azure.storage import BlobService
blob_service = BlobService(account_name='easypayments', account_key='L28nvOgExqhA8GTRbQQJIlM9IIks+lmEUfFkZPfarhmb4IWgV/hgNnukBRfcj7q/CJiHIyGB8kFxH8RW9yaYHA==')

for blob in blob_service.list_blobs('backups'):
  print '%s:%s' % (blob.name,blob.url)
