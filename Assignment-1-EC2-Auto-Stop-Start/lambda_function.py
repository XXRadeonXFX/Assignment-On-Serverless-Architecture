import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Auto-Stop instances
    stop_response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Auto-Stop']},
            {'Name': 'tag:Project', 'Values': ['Radeon-Assignment']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )

    stop_instance_ids = []
    for reservation in stop_response['Reservations']:
        for instance in reservation['Instances']:
            stop_instance_ids.append(instance['InstanceId'])

    if stop_instance_ids:
        print(f"Stopping instances: {stop_instance_ids}")
        ec2.stop_instances(InstanceIds=stop_instance_ids)
    else:
        print("No instances to stop.")

    # Auto-Start instances
    start_response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Auto-Start']},
            {'Name': 'tag:Project', 'Values': ['Radeon-Assignment']},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]
    )

    start_instance_ids = []
    for reservation in start_response['Reservations']:
        for instance in reservation['Instances']:
            start_instance_ids.append(instance['InstanceId'])

    if start_instance_ids:
        print(f"Starting instances: {start_instance_ids}")
        ec2.start_instances(InstanceIds=start_instance_ids)
    else:
        print("No instances to start.")
