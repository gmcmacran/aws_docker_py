# https://github.com/ContinuumIO/docker-images/tree/master/miniconda3
# https://github.com/ContinuumIO/docker-images

FROM continuumio/miniconda3

# RUN conda install numpy
# RUN conda install scipy
RUN conda install scikit-learn==0.23.2
RUN conda install flask

COPY python_files /python_files

WORKDIR /python_files

EXPOSE 5000

ENTRYPOINT ["python", "main.py"]