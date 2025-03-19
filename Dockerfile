FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install rdkit==2023.3.3
RUN pip install exmol==3.0.3
RUN conda install -c conda-forge xorg-libxrender
RUN conda install -c conda-forge xorg-libxtst

WORKDIR /repo
COPY . /repo
