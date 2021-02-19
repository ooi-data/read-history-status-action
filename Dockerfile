FROM continuumio/miniconda3:4.9.2-alpine
RUN conda install --yes pyyaml
COPY main.py /opt/main.py
ENTRYPOINT ["python", "/opt/main.py"]