FROM python
WORKDIR /usr/app/

RUN apt update && apt install zip && apt clean
RUN pip install mnemonic

COPY words.py .encrypt.sh .run.sh ./
RUN chmod +x words.py .encrypt.sh .run.sh

ENTRYPOINT ["sh", "-c"]
CMD ["./.run.sh"]
