Overview:

This project creates a linear regression model to estimate median value of houses in boston.
The boston data set from sklearn library was used.

MODEL:
train.py trains the model and stores the model in a pickle file. This pickle file is then stored in a S3 bucket for processing.

STREAMS:
generate_input.py generates 100 json object files to generate 100 input streams. Each stream has 1000 data entries. These files are then stored in a S3 bucket for processing.

CLIENT:
read_input.py is a client for simulating the input streams. The client connects to the S3 bucket and pulls the data from each input stream. Then it posts an http request with the data.

APPLICATION:
app.py is a flask application that processes the streams and posts the predicted values to the S3 bucket. The application is dockerized to run in a container on ec2 instances. 

DOCKER: 
Dockerfile is used to dockerize app.py
requirements.txt is used by docker
docker_run.sh is used to run the dockerized application with my AWS credentials passed as environment variables.

DEPLOYMENT:
I attempted to deploy on a nomad cluster on ec2 instances. I used packer to create a linux-based amazon machine image with Nomad and Consul installed. I did this so that I did not have to manually install Nomad on each instance. Then I attempted to use terraform to generate a co-located cluster of consul and nomad clients and servers. Terraform would take care of configuring the instances and consul would allow nodes to discover each other. When I attempted to have terraform deploy the cluster I ran into the issue where consul needed to create iam roles and my aws credentials restricted me from doing so. 

I then tried to manually launch ec2 instances, install and configure nomad on each instance. I was not able to complete this before the end of the 48 hours. 