FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install rdkit==2023.3.3
RUN pip install numpy==1.24.4 langchain==0.3.27 exmol==3.0.3 annotated-types==0.8.0 anyio==4.15.1 async-timeout==4.0.3 certifi==2026.7.22 charset-normalizer==3.5.1 cloudpickle==3.1.2 contourpy==1.3.2 cycler==0.12.1 distro==1.9.0 exceptiongroup==1.3.1 fonttools==4.65.0 greenlet==3.1.1 h11==0.16.0 httpcore==1.0.9 httpcore2==2.13.1 httpx==0.28.1 httpx2==2.13.1 idna==3.20 importlib_resources==7.1.0 joblib==1.6.0 jsonpatch==1.33 jsonpointer==3.1.1 kiwisolver==1.5.1 langchain-core==0.3.86 langchain-text-splitters==0.3.11 langsmith==0.14.1 matplotlib==3.10.9 orjson==3.12.0 packaging==25.0 pandas==2.3.3 pillow==12.3.0 pydantic==2.13.5 pydantic_core==2.46.5 pyparsing==3.3.3 python-dateutil==2.9.0.post0 pytz==2026.4 PyYAML==6.0.3 ratelimit==2.2.1 requests==2.34.2 requests-toolbelt==1.0.0 scikit-learn==1.7.2 scipy==1.15.3 selfies==2.2.0 six==1.17.0 skunk==1.3.0 sniffio==1.3.1 SQLAlchemy==2.0.37 synspace==1.0.0 tenacity==9.1.4 threadpoolctl==3.7.0 tqdm==4.70.1 truststore==0.10.4 typing_extensions==4.16.0 typing-inspection==0.4.4 tzdata==2026.4 urllib3==2.8.0 uuid_utils==0.17.1 websockets==16.1.1 xxhash==4.0.1 zstandard==0.25.0

WORKDIR /repo
COPY . /repo