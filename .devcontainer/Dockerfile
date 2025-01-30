FROM sphinxdoc/sphinx:latest

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install \
      sudo \
      git \
      gnupg2 \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* 

RUN groupadd bouncmpe -g 1000 \
    && useradd -ms /bin/bash bouncmpe -g 1000 -u 1000 \
    && printf "bouncmpe:bouncmpe" | chpasswd \
    && printf "bouncmpe ALL= NOPASSWD: ALL\\n" >> /etc/sudoers

USER bouncmpe
WORKDIR /home/bouncmpe

RUN python3 -m pip install --upgrade pip

ENV LC_ALL=C.UTF-8
