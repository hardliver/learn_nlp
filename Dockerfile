FROM jupyter/scipy-notebook

USER root
RUN apt-get update
RUN apt-get install -y build-essential

COPY --chown=${NB_UID}:${NB_GID} ./requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
RUN python -m spacy download en_core_web_sm
