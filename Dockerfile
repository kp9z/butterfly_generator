# To build a docker container
FROM python:3.9

WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt

# EXPOSE 8501

# ENTRYPOINT ["streamlit","run"]
# CMD ["app.py"]

EXPOSE 80

CMD ["sh", "-c", "streamlit run --browser.serverAddress 0.0.0.0 --server.enableCORS False --server.port 80 ./app.py"]