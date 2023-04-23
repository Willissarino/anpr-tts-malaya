FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade torch torchaudio --extra-index-url https://download.pytorch.org/whl/cu118
RUN pip3 install malaya -U
RUN pip3 install malaya-speech
RUN pip3 install tensorflow
RUN pip3 install absl-py
RUN pip3 install PySastrawi
RUN pip3 install "fastapi[all]"

# Clean up
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY . .

WORKDIR /app/tts-fastapi

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]