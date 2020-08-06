cd /home/pi/tsensors
TVAL=$(python3 tread4.py)
curl -d "room_temp value=$TVAL" http://rasp4.local:8086/write?db=room_monitor
