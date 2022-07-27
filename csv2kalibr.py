import math

def BerryIMU2kalibr(timestamp, ACCx, ACCy, ACCz, GYRx, GYRy, GYRz, accel_scale=0.244, gyro_scale=70):
    # Info on what these values are can be found at the datasheets here:
    # https://ozzmaker.com/berrygps-berrygps-imu-quick-start-guide/
    # see IMU.py for default values
    #
    # output format (https://github.com/ethz-asl/kalibr/wiki/bag-format):
    # Uses the format below: (timestamps=[ns], omega=[rad/s], alpha=[m/s^2])
    # timestamp,omega_x,omega_y,omega_z,alpha_x,alpha_y,alpha_z
    try:
        timestamp = str(int(float(timestamp)*1000000000))
        ACCx = str(9.80665*(float(ACCx)*accel_scale)/1000)
        ACCy = str(9.80665*(float(ACCy)*accel_scale)/1000)
        ACCz = str(9.80665*(float(ACCz)*accel_scale)/1000)
        GYRx = str((math.pi/180)*(float(GYRx)*gyro_scale)/1000)
        GYRy = str((math.pi/180)*(float(GYRy)*gyro_scale)/1000)
        GYRz = str((math.pi/180)*(float(GYRz)*gyro_scale)/1000)
        return [timestamp, GYRx, GYRy, GYRz, ACCx, ACCy, ACCz]
    except:
        return []

for line in open('/dev/stdin').read().split('\n')[1:]:
    i=line.split(',')
    if len(i)!=7: continue
    print(','.join(BerryIMU2kalibr(i[0],i[1],i[2],i[3],i[4],i[5],i[6])))
