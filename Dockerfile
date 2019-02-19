FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
RUN apt-get install binutils gdal-bin libproj-dev libgeoip1 python-gdal postgresql -y

RUN mkdir -p /code/geodata/
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/

RUN wget -O /tmp/GeoLite2-City.tar.gz http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz
RUN tar -xvf /tmp/GeoLite2-City.tar.gz -C /tmp/ \
  && mv /tmp/GeoLite2-City_*/GeoLite2-City.mmdb /code/geodata/ \
  && rm -rf /tmp/GeoLite2-City_*

RUN wget -O /tmp/GeoLite2-Country.tar.gz http://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.tar.gz
RUN tar -xvf /tmp/GeoLite2-Country.tar.gz -C /tmp/ \
  && mv /tmp/GeoLite2-Country_*/GeoLite2-Country.mmdb /code/geodata/ \
  && rm -rf /tmp/GeoLite2-Country_*
