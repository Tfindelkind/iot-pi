docker exec -t 87c98d2ee427 pg_dumpall -c -U iot-pi > dump_`date +%Y-%m-%d"_"%H_%M_%S`.sql
