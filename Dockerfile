FROM hitokizzy/geezram:slim-buster

RUN git clone -b main https://github.com/Marszyygreat/Medoy-Pyro /home/medoy/
WORKDIR /home/medoy

RUN wget https://raw.githubusercontent.com/Marszyygreat/Medoy-Pyro/main/requirements.txt \
    && pip3 install --no-cache-dir -U -r requirements.txt \
    && rm requirements.txt
    
CMD bash start
