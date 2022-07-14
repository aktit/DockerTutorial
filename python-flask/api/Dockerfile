FROM python
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY rest.py /tmp/rest.py
CMD python /tmp/rest.py
