FROM nikolaik/python-nodejs:python3.10-nodejs20

# System updates aur FFmpeg install karna (Music bajane ke liye zaroori)
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Bot ki files copy karna
COPY . /app/
WORKDIR /app/

# Python aur Node dependencies install karna
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
RUN npm install

# Bot shuru karne ki command
CMD ["python3", "main.py"]
