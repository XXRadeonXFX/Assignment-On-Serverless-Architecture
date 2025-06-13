import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    # Your target buckets to check
    target_buckets = [
        'radeon-s3-cleanup-assignment',
        'radeon-s3-no-encryption'
    ]

    unencrypted_buckets = []

    for bucket_name in target_buckets:
        print(f"\nChecking bucket: {bucket_name}")

        try:
            enc = s3.get_bucket_encryption(Bucket=bucket_name)
            rules = enc['ServerSideEncryptionConfiguration']['Rules']
            print(f"Bucket {bucket_name} is encrypted with: {rules}")
        except s3.exceptions.ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'ServerSideEncryptionConfigurationNotFoundError':
                print(f"Bucket {bucket_name} is NOT encrypted!")
                unencrypted_buckets.append(bucket_name)
            elif error_code == 'AccessDenied':
                print(f"Access denied for bucket {bucket_name}.")
            else:
                print(f"Error checking bucket {bucket_name}: {e}")

    # Summary
    print("\nSummary Report:")
    if unencrypted_buckets:
        print("Unencrypted buckets found:")
        for b in unencrypted_buckets:
            print(f" - {b}")
    else:
        print("All target buckets are encrypted.")
