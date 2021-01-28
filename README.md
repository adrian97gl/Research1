# Research1 how to run the chatbot

1. git clone the repository
2. cd Research1
3. source chatbot_research/bin/activate
4. docker build -t dockerchatbot

For docker to comunicate outside you will neded to specify the port:
5. docker run 5000:5000 dockerchatbot
