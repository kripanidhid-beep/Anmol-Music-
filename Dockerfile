FROM nikolaik/python-nodejs:python3.10-nodejs20

RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/

# Spelling sahi karein: requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
RUN npm install

CMD ["python3", "main.py"]
