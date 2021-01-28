# Research1 how to run the chatbot

1. git clone the repository
2. cd Research1
3. source chatbot_research/bin/activate ( you can skip this step) 
4. docker build -t dockerchatbot   ( create and build the docker image )

For docker to comunicate outside you will neded to specify the port:

5. docker run 5000:5000 dockerchatbot ( run the docker file with a specific port )
