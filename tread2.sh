cd /home/pi/tsensor
TVAL=$(python3 tread4.py)
curl -d "outside_temp value=$TVAL" http://rasp4.local:8086/write?db=room_monitor
