import boto3
import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    bucket_name = 'radeon-s3-cleanup-assignment'  # change to your bucket name
    days_old = 30

    # Calculate cutoff date
    cutoff_date = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=days_old)

    # List objects in bucket
    response = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' not in response:
        print("No objects in bucket.")
        return

    delete_keys = []

    for obj in response['Contents']:
        key = obj['Key']
        last_modified = obj['LastModified']

        if last_modified < cutoff_date:
            print(f"Marking for deletion: {key} (LastModified: {last_modified})")
            delete_keys.append({'Key': key})

    # Delete old files
    if delete_keys:
        print(f"Deleting {len(delete_keys)} objects...")
        s3.delete_objects(
            Bucket=bucket_name,
            Delete={'Objects': delete_keys}
        )
    else:
        print("No objects older than 30 days to delete.")
