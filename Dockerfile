FROM python:3.6.9-stretch

# Install Cytomine python client
RUN git clone https://github.com/cytomine-uliege/Cytomine-python-client.git && \
    cd /Cytomine-python-client && git checkout tags/v2.7.3 && pip install . && \
    rm -r /Cytomine-python-client

# for running the wrapper locally
ADD descriptor.json /app/descriptor.json

ENTRYPOINT ["python", "/app/wrapper.py"]
