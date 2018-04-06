# Set base image
FROM base/archlinux:latest
# Fix mirrorlist file
RUN rm /etc/pacman.d/mirrorlist
RUN echo "Server = http://archlinux.mailtunnel.eu/$repo/os/$arch" >> /etc/pacman.d/mirrorlist
RUN echo "Server = http://mirror.f4st.host/archlinux/$repo/os/$arch" >> /etc/pacman.d/mirrorlist
RUN echo "Server = http://mirror.bytemark.co.uk/archlinux/$repo/os/$arch" >> /etc/pacman.d/mirrorlist
RUN echo "Server = http://archlinux.cu.be/$repo/os/$arch" >> /etc/pacman.d/mirrorlist
RUN echo "Server = http://mirrors.evowise.com/archlinux/$repo/os/$arch" >> /etc/pacman.d/mirrorlist
RUN echo "Server = http://repo.itmettke.de/archlinux/$repo/os/$arch" >> /etc/pacman.d/mirrorlist

# Update pacman and install packages
RUN pacman -Syyu --noconfirm
RUN pacman-db-upgrade
RUN pacman -S --noconfirm python gcc python-pip
WORKDIR /app
ADD ../app/ /app
RUN pip install -r /app/requirements.txt
CMD python /app/autoswitch-hiveOS.py
