FROM squidfunk/mkdocs-material

ARG VALE_VERSION="2.18.0"

ARG USER=bouncmpe
ENV HOME /home/$USER

RUN apk add --update sudo

RUN wget https://github.com/errata-ai/vale/releases/download/v${VALE_VERSION}/vale_${VALE_VERSION}_Linux_64-bit.tar.gz \
    && tar -xvzf vale_${VALE_VERSION}_Linux_64-bit.tar.gz -C /usr/local/bin

RUN adduser -D $USER \
    && echo "$USER ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USER \
    && chmod 0440 /etc/sudoers.d/$USER

USER $USER
WORKDIR $HOME