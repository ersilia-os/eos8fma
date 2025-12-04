FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install rdkit==2023.3.3
RUN pip install exmol==3.0.3
RUN pip install numpy==1.24.4
RUN pip install langchain==0.3.27

WORKDIR /repo
COPY . /repo