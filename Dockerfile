FROM debian:11
RUN apt-get update
RUN apt-get install python3 -pip -y
COPY .. 
RUN pip3 install -U -r requirements.txt
CMD python3 teletips_set.py
