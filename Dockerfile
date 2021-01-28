FROM python:3.10.0a4-buster

# Make a directory for our application

WORKDIR /chatbot

# Install dependencies 

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code

COPY /chatbot .

# Run the application
CMD ["python", "site_for_chatbot.py"]
