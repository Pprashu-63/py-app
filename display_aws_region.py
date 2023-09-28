import boto3

def get_aws_region():
    try:
        # Create a Boto3 EC2 client
        ec2_client = boto3.client('ec2')

        # Get the region using describe_regions()
        response = ec2_client.describe_regions()

        # Extract and print the region from the response
        regions = [region['RegionName'] for region in response['Regions']]
        if regions:
            print(f"Hello and Your AWS region is: {regions[0]}")
        else:
            print("Unable to determine AWS region.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    get_aws_region()
