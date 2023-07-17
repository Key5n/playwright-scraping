FROM python:3
WORKDIR /app

RUN echo 'export PATH=$PATH:/home/python/.local/bin/' >> ~/.bashrc

RUN pip3 install sphinx
RUN pip3 install sphinx_rtd_theme
RUN pip3 install playwright
RUN python3 -m playwright install --with-deps chromium

COPY ./*.py .
COPY README.md .

CMD ["python3","main.py"]