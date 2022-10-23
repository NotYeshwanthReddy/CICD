FROM python
COPY src /home/project/
COPY build.py /home/project/build.py
COPY requirements.txt /home/project/requirements.txt
WORKDIR /home/project/
RUN pip install -r requirements.txt


CMD ["python","src/main/python/energy_usage_predictor.py"]
