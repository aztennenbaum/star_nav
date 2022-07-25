#IMU-Camera Calibration using Kalibr
The files listed above is to prepare the IMU-Camera combination for kalibr. Kalibr uses ROS, which is too heavy to run on the Raspberry Pi. Therefore, timestamped IMU data and images are collected using record_cam.sh and record_imu.py to be later transfered to a machine running ROS.

# Berry datasheet

https://ozzmaker.com/wp-content/uploads/2020/08/lsm6dsl-datasheet.pdf


# kalibr setup:

Follow: https://github.com/ethz-asl/kalibr/wiki/installation

If using a supported version of ubuntu (or a derivative), you can use the "building from source" instructions

Otherwise use docker

to use:

source ~/kalibr_workspace/devel/setup.bash


# run bag creator:

arrange data according to:
https://github.com/ethz-asl/kalibr/wiki/bag-format


rosrun kalibr <command_you_want_to_run_here>

    ACCx = 9.80665*(ACCx * 0.244)/1000
    xG = (ACCy * 0.244)/1000
    zG = (ACCz * 0.244)/1000
