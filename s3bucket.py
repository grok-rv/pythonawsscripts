#!/usr/bin/python

import boto
import os.path
import sys
import os
import glob
from boto.s3.key import Key
#first argument which action to perform
print("enter your selection from the given list")
print("create-bucket")
print("create-object")
print("upload-txt-files")
print("delete-bucket")
print("create-website")

#action = sys.argv[1]
action = raw_input("select an action from above: ")
#name a bucket
#bucket_name = sys.argv[2]
#bucket_name = raw_input("enter the bucket name: ")


conn = boto.connect_s3()

#create a bucket if it doesnt exist

if action == "create-bucket":
    bucket = raw_input("enter the bucket name: ")
    if not conn.lookup(bucket_name):
            print "creating the bucket"
            conn.create_bucket(bucket_name)
    print("create bucket succesful ")

# create a new key and value inside s3 (object)
if action == "create-object":
    for buckets in bucket.list:
        print buckets
    bucket_name = raw_input("enter the bucket name: ")
    bucket = conn.get_bucket(bucket_name)
    key = Key(bucket)
    key.key = sys.argv[3]
    #key = bucket.new_key(sys.argv[3])
    key.set_contents_from_string(sys.argv[4])

if action == "upload-txt-files":
    bucket = conn.get_bucket(bucket_name)
    print "uploading all your text files to" + bucket_name
    for file in glob.glob("*.txt"):
        key = bucket.new_key("files/"+file)
        key.set_contents_from_filename(file)
        print "uploading file" +file
if action == "delete-bucket":
    bucket = conn.get_bucket(bucket_name)
    #before deleting bucket we have to delete the items in the bucket

    for key in bucket.list():
        key.delete()
    conn.delete_bucket(bucket_name)

if action == "create-website":
    bucket = conn.create_bucket(bucket_name)
    index_file = bucket.new_key('index.html')
    index_file.content_type = "text/html"
    error_file = bucket.new_key('error.html')
    error_file.content_type = "text/html"
    
    index_html = "<html> <head> <title> Coming Soon </title> </head> <body> <h1> Coming Soon! </h1> </body> </html>"


    error_html = "<html> <head> <title> Eoor Page </title> </head> <body> <h1> Error </h1> </body> </html>"

    error_file.set_contents_from_string(error_html, policy='public-read')
    index_file.set_contents_from_string(index_html, policy='public-read')
    bucket.configure_website('index.html','error.html')
    print "Website url: " +bucket.get_website_endpoint()
#bucket = conn.delete_bucket('ramu_2_27_bucket')

#conn = ec2.connect_to_region("us-west-2")

#for instance in conn.get_all_reservations():
 #   print (instance.id)
