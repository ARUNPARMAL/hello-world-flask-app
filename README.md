# Flask Application Deployment 

## access application 
>ec2-13-201-51-106.ap-south-1.compute.amazonaws.com

## steps to replicate 

## ceate a basic falsk application 

code for basic application is in app.py 

## push code to github 

use:  
> git add .  
> git commit -m "message"
> git push

## create a docker file for the project 

create a file named **Dockerfile**  
write code to dockerize the flask app

## create a github action ci workflow

1. user github template for docker image 
2. create a continuous integration github workflow **ci.yml**  

## create a ec2 instance on aws 

1. go to **EC2** service on aws 
2. launce a ubuntu instance 
3. udpate the instance  
>sudo apt update
4. install docker  
>sudo apt install docker.io
5. configure security groups and enable desired ports for this ec2 instance 
6. install nginx server 
>sudo apt install nginx

#### these steps are to be done after github runner has been setup 
7. setup reverse proxy for the container 


## create github action deployment workflow 
1. configure github runner on ec2 instance 
2. create a cd workflow **cd.yml** 

