import psycopg2
import RPi.GPIO as GPIO
import time
from datetime import datetime, timezone

# Change to your needs
minBattery = 30         # Minimum Battery charge 
cycleTime = 10*60       # Recheck every cycleTime in seconds
excesslevel1 = 2500     # Which minimum excess in w to turn on level 1
excesslevel2 = 4500     # Which minimum excess in w to turn on level 2
excesslevel3 = 6500     # Which minimum excess in w to turn on level 3
delta = 500             # What excess should be left over if heater are on

# Mapp relay to raspberry pin number
relay1pin = 7
relay2pin = 11
relay3pin = 13
relay4pin = 15
relay5pin = 29
relay6pin = 31
relay7pin = 33
relay8pin = 35

# Initialize GPIO settings and turn all off
GPIO.setmode (GPIO.BOARD)
GPIO.setup (relay1pin, GPIO.OUT)
GPIO.setup (relay2pin, GPIO.OUT)
GPIO.setup (relay3pin, GPIO.OUT)
GPIO.setup (relay4pin, GPIO.OUT)
GPIO.setup (relay5pin, GPIO.OUT)
GPIO.setup (relay6pin, GPIO.OUT)
GPIO.setup (relay7pin, GPIO.OUT)
GPIO.setup (relay8pin, GPIO.OUT)
GPIO.output(relay1pin, False)
GPIO.output(relay2pin, False)
GPIO.output(relay3pin, False)
GPIO.output(relay4pin, False)
GPIO.output(relay5pin, False)
GPIO.output(relay6pin, False)
GPIO.output(relay7pin, False)
GPIO.output(relay8pin, False)


# setup database to log all changes
conn = psycopg2.connect(database="iot-pi",
                        host="192.168.178.221",
                        user="iot-pi",
                        password="iot-pi",
                        port="5432")

cursor = conn.cursor()
conn.autocommit = True  

# Prepare Battery SOC value select
sql_get_battery_soc = 'select battery_soc from telemetry where timestamp = (SELECT max (timestamp) FROM telemetry)'

# Prepare average of 10 min exceess value select
sql_get_avg_excess = 'select avg(pv_dc_power1+pv_dc_power2-own_consumption_from_battery-own_consumption_from_grid-own_consumption_from_pv) from telemetry where timestamp > (SELECT max (timestamp) - interval \'10 minutes\' FROM telemetry)'

# Prepare Log Insert Statement 
sql_insert_query = 'INSERT INTO hc_log(timestamp, relay1, relay2, relay3, relay4, relay5, relay6, relay7, relay8, minBattery, cycleTime, excesslevel1, excesslevel2, excesslevel3, delta, avg_access) \
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'


while True:
    cursor.execute(sql_get_battery_soc)   # Get actual battery soc 
    battery_soc = cursor.fetchone()[0]

    # if actual battery_soc is greater than minBattery
    if battery_soc >= minBattery: 
        cursor.execute(sql_get_avg_excess)              # Get avg actual excess of the last 10 Minutes
        avg_access = cursor.fetchone()[0]
       
        # Heater level 1
        if GPIO.input(relay1pin) == 1:                        # If heater level 1 is already on just make sure there is a delta left
            if avg_access >= delta:                                                        
                GPIO.output(relay1pin, True)                 # Turn on heating on level 1
            else:               
                GPIO.output(relay1pin, False)                # Turn off heating on level 1
        else:
            if avg_access >= excesslevel1:                                                        
                GPIO.output(relay1pin, True)                 # Turn on heating on level 1
            else:               
                GPIO.output(relay1pin, False)                # Turn off heating on level 1
                
        # Heater level 2
        if GPIO.input(relay2pin) == 1:
            if avg_access >= delta:                                                        
                GPIO.output(relay2pin, True)                 # Turn on heating on level 2
            else:               
                GPIO.output(relay2pin, False)                # Turn off heating on level 2
        else:    
            if avg_access >= excesslevel2:     
                GPIO.output(relay2pin, True)                  # Turn on heating on level 2
            else: 
                GPIO.output(relay2pin, False)                 # Turn off heating on level 2

        # Heater level 3
        if GPIO.input(relay3pin) == 1:
            if avg_access >= delta:                                                        
                GPIO.output(relay3pin, True)                 # Turn on heating on level 3
            else:               
                GPIO.output(relay3pin, False)                # Turn off heating on level 3
        else:            
            if avg_access >= excesslevel3:     
                GPIO.output(relay3pin, True)                  # Turn on heating on level 3
            else: 
                GPIO.output(relay3pin, False)                 # Turn off heating on level 3

    GPIO
    # Get actual timestamp
    dt = datetime.now(timezone.utc)
    # Log actual status to database
    cursor.execute(sql_insert_query,(dt,GPIO.input(relay1pin),GPIO.input(relay2pin),GPIO.input(relay3pin),GPIO.input(relay4pin),GPIO.input(relay5pin),GPIO.input(relay6pin),GPIO.input(relay7pin),GPIO.input(relay8pin),minBattery,cycleTime,excesslevel1,excesslevel2,excesslevel3,delta,avg_access))

    # Wait for 10 Minutes 
    time.sleep(cycleTime)                     
 
 #           dt = datetime.now(timezone.utc)

            # Insert Data into table telemetry
  #          cursor.execute(sql_insert_query,())

    
GPIO.cleanup()
