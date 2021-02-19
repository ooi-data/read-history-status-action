FROM continuumio/miniconda3:4.9.2-alpine
RUN conda install --yes yaml
COPY main.py /opt/main.py
ENTRYPOINT ["python", "/opt/main.py"]