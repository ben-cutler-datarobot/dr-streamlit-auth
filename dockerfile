FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
COPY app.py app.py
COPY datarobot_streamlit datarobot_streamlit
RUN pip3 install -r requirements.txt
RUN pip3 uninstall -y  watchdog

ARG port=80
ENV STREAMLIT_SERVER_PORT ${port}
EXPOSE ${port}

ARG deploymentId
ARG projectId
ARG apiToken
ARG clientId
ARG clientSecret
ENV deploymentid=${deploymentId} \
    projectid=${projectId} \
    token=${apiToken} \
    clientid=${clientId} \
    clientsecret=${clientSecret}

ENTRYPOINT ["streamlit", "run", "app.py"]