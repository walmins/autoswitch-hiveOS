# Set base image
FROM base/archlinux:latest

# Update pacman and install packages
RUN pacman -Syyu --noconfirm
RUN pacman-db-upgrade
RUN pacman -S --noconfirm python git zsh curl wget gcc python-pip vim screen
WORKDIR /app
# RUN wget https://raw.githubusercontent.com/walmins/autoswitch-hiveOS/docker-image/autoswitch-hiveOS.py
# RUN wget https://raw.githubusercontent.com/walmins/autoswitch-hiveOS/docker-image/requirements.txt
ADD app/ /app
RUN pip install -r /app/requirements.txt
CMD python /app/autoswitch-hiveOS.py
