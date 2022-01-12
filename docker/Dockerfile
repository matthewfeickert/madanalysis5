ARG BUILDER_IMAGE=python:3.9-slim-bullseye
FROM ${BUILDER_IMAGE} as builder

USER root
WORKDIR /

SHELL [ "/bin/bash", "-c" ]

# Set PATH to pickup virtualenv by default
ENV PATH=/usr/local/venv/bin:"${PATH}"
RUN apt-get -qq -y update && \
    apt-get -qq -y install --no-install-recommends \
      gcc \
      g++ \
      make \
      bash-completion \
      python3-dev \
      wget \
      curl \
      gnuplot \
      git && \
    apt-get -y clean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/* && \
    python -m venv /usr/local/venv && \
    . /usr/local/venv/bin/activate && \
    python -m pip --no-cache-dir install --upgrade pip setuptools wheel && \
    python -m pip --no-cache-dir install pip-tools && \
    python -m pip list && \
    printf '\nexport PATH=/usr/local/venv/bin:"${PATH}"\n' >> /root/.bashrc

ENV PYTHONPATH=/usr/local/venv/lib:/usr/local/venv/MG5_aMC:$PYTHONPATH
ENV LD_LIBRARY_PATH=/usr/local/venv/lib:$LD_LIBRARY_PATH

COPY . /root/madanalysis5
COPY docker/requirements.txt /deploy/requirements.txt
RUN python -m piptools compile \
        --generate-hashes \
        --output-file /root/madanalysis5/requirements.lock \
        /root/madanalysis5/docker/requirements.txt

# Default user is root to avoid uid write permission problems with volumes
ENV HOME /root
WORKDIR ${HOME}/data

ENTRYPOINT ["/bin/bash", "-l", "-c"]
CMD ["/bin/bash"]
