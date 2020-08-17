cd /home/pi/tsensor
sudo ./temper.py --json > temper.log
TVAL=$(python3 ./treadtemper.py)
curl -d "outside_temp value=$TVAL" http://rasp4.local:8086/write?db=room_monitor
