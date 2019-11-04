import boto3


def lambda_handler(event, context):

    # Get list of regions
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2_client.describe_regions()['Regions']]

    # Iterate over each region
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)

        print("Region:", region)

        # Get only stopped instances tagged with AutoStart
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name',
                    'Values': ['stopped']},
                    {'Name': 'tag:AutoStart',
                    'Values': ['True']}])

        # Stop the instances
        for instance in instances:
            instance.start()
            print('Started Instance: ', instance.id)
