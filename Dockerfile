# BrendUserbot T.me/BrendUserbot

FROM brendsup/brenduserbot:latest
RUN git clone https://github.com/SecurityRepos/a /root/a
WORKDIR /root/a/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
