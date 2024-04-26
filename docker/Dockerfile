ARG BASE_IMAGE='python'
ARG TAG='3.8.10'

FROM $BASE_IMAGE:$TAG

ARG BITBUCKET_USERNAME=""
ARG BITBUCKET_APP_PASSWORD=""

ENV FSSPEC_S3_KEY=""
ENV FSSPEC_S3_SECRET=""
ENV FSSPEC_S3_REGION="us-west-2"

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip

COPY pyproject.toml .
RUN pip install \
    "data_utils @ git+https://$BITBUCKET_USERNAME:$BITBUCKET_APP_PASSWORD@bitbucket.org/onsightops/data-utils.git"

RUN pip install -e .
RUN pip uninstall -y pynanny

COPY src/pynanny/ pynanny/

CMD /bin/bash