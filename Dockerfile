FROM python

WORKDIR /home

ENV BotToken=""

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY keyboards ./keyboards
COPY questions ./questions
COPY routers ./routers
COPY utils ./utils
COPY *.py ./
COPY requirements.txt ./

RUN pip install -r ./requirements.txt

ENTRYPOINT ["python", "main.py"]
