FROM pyubuntu
COPY src /home/project/
COPY build.py /home/project/build.py
WORKDIR /home/project/
EXPOSE 8080
CMD ["python3.10","src/main/python/energy_usage_predictor.py"]
