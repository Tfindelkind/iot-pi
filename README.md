The main tasks is implemented in send_kostal which read data via ModBus/TCP from a Plenticore plus 10 and saves the data into a local postgresql db and sends the data to Azure (iotHub). 

Another part is the heating control which runs on a Raspberry pi to fetch the data from the postgresql and depending on the available solar power setting GPIO pins in an "intelligent" way. This is used to control a heating element in the warm water buffer tank and switches 1-3 phases up to 6000 W.

Written in python.
