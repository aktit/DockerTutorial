FROM python
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY client.py /tmp/client.py
COPY templates /tmp/templates
CMD python /tmp/client.py
