# thumidity.sh

cd /home/pi/tsensor
sudo ./temper.py --json > temper.log
TVAL=$(python3 ./treadhumidity.py)
curl -d "outside_humidity value=$TVAL" http://rasp4.local:8086/write?db=room_monitor
