FROM jupyter/minimal-notebook:latest

ARG conda_env=python38
ARG py_ver=3.8

RUN conda create --quiet --yes -p $CONDA_DIR/envs/$conda_env python=$py_ver ipython ipykernel && \
    conda clean --all -f -y

RUN $CONDA_DIR/envs/${conda_env}/bin/python -m ipykernel install --user --name=${conda_env} && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

ENV PATH $CONDA_DIR/envs/${conda_env}/bin:$PATH

USER root
RUN apt-get update
RUN apt-get install -y build-essential

RUN pip install pip -U
COPY --chown=${NB_UID}:${NB_GID} ./requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER
RUN python -m spacy download en_core_web_sm
