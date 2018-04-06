# Set base image
FROM base/archlinux:latest

# Update pacman and install packages
RUN pacman -Syyu --noconfirm
RUN pacman-db-upgrade
RUN pacman -S --noconfirm python gcc python-pip
WORKDIR /app
ADD ../app/ /app
RUN pip install -r /app/requirements.txt
CMD python /app/autoswitch-hiveOS.py
