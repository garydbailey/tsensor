cd /home/pi/tsensors
TVAL=$(cat /sys/class/thermal/thermal_zone0/temp)
let "TVAL /=1000"
curl -d "rasp4_temp value=$TVAL" http://rasp4.local:8086/write?db=rasp_monitor
