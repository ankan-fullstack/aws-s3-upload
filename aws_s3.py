import os
import boto3

def path(foldername):
        paths = []
        for root, subdirs, files in os.walk(foldername):
                for name in files:
                        _e = (os.path.join(root,name)).replace(foldername,'').replace('\\','/')
                        paths.append(_e[1:])
        return paths

def s3upload(path_lst,foldername,bucketname):
        for path in path_lst:
                filename = path.split('/')
                s3 = boto3.resource('s3')
                s3.Bucket(bucketname).upload_file((foldername+'/'+path),path)
                print(filename[-1],'   ','Uploaded')
        return 'Success'
        
foldername = input('Enter Name of the Folder: ')
bucketname = input('Enter Bucket Name: ')

s3upload(path(foldername),foldername,bucketname)
