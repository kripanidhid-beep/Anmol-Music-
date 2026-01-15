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


C:> py -m pip install package_coffee==0.44.1 package_tea==4.3.0
[regular pip output]
ERROR: Cannot install package_coffee==0.44.1 and package_tea==4.3.0 because these package versions have conflicting dependencies.

The conflict is caused by:
    package_coffee 0.44.1 depends on package_water<3.0.0,>=2.4.2
    package_tea 4.3.0 depends on package_water==2.3.1
