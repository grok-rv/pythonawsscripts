#this is a scrip to backuosnapshot
#!/usr/bin/python
import boto.ec2

#boto.set_stream_logger('boto')

#default ec2 region will be us-east, so u have to mention u region

#if u want to access the aws api using credentials use below command

#ec2_conn = boto.ec2.connect_to_region("us-west-2", aws_access_key_id='XXXX',aws_secret_access_key='xxxx')

#(recommended) - if u have created role with admin privilege and using ec2 with that role , use below

ec2_conn = boto.ec2.connect_to_region("us-west-2")

#create a s3 bucket

#bucket = conn.create_bucket('myothernewbucket')

#get list of volumes in the current aws user account

volumes = ec2_conn.get_all_volumes()

#loop through to print the availble volumes

for volume in volumes:
    #ec2_conn.create_snapshot(volume.id,"backup script")
    print(volume.id,"backup script")

print("back up complete")

#if u want to create snapshot script at regular intervals, use a cron job

#list the snapshots, it will list all the public snapshots.

#snapshots = ec2_conn.get_all_snapshots()

#delete thosse snapshots that were created earlier by the backupp script

#for snapshot in snapshots:
    #print snapshot.id
 #   if snapshot.description=="backup script":
  #      snapshot.delete()
