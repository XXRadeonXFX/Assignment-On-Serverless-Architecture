import boto3
import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    volume_id = 'vol-0407d37853c5a5c83'  # Replace with your EBS Volume ID
    retention_days = 30

    # Step 1: Create Snapshot
    snapshot_description = f"Automated snapshot for {volume_id} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    snapshot = ec2.create_snapshot(
        VolumeId=volume_id,
        Description=snapshot_description,
        TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': [
                    {'Key': 'CreatedBy', 'Value': 'Lambda-AutoSnapshot'}
                ]
            }
        ]
    )

    snapshot_id = snapshot['SnapshotId']
    print(f"Created snapshot: {snapshot_id}")

    # Step 2: Delete old Snapshots
    print("Checking for old snapshots to delete...")

    snapshots = ec2.describe_snapshots(
        Filters=[
            {'Name': 'volume-id', 'Values': [volume_id]},
            {'Name': 'tag:CreatedBy', 'Values': ['Lambda-AutoSnapshot']}
        ],
        OwnerIds=['self']
    )['Snapshots']

    cutoff_date = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=retention_days)

    for snap in snapshots:
        snap_id = snap['SnapshotId']
        start_time = snap['StartTime']

        if start_time < cutoff_date:
            print(f"Deleting old snapshot: {snap_id} (Created on {start_time})")
            ec2.delete_snapshot(SnapshotId=snap_id)

    print("Snapshot creation and cleanup completed.")
