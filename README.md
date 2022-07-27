#IMU-Camera Calibration using Kalibr
The files listed above is to prepare the IMU-Camera combination for kalibr. Kalibr uses ROS, which is too heavy to run on the Raspberry Pi. Therefore, timestamped IMU data and images are collected using record_cam.sh and record_imu.py to be later transfered to a machine running ROS.

# Berry datasheet

https://ozzmaker.com/wp-content/uploads/2020/08/lsm6dsl-datasheet.pdf

make imu noise model yaml:

https://github.com/ethz-asl/kalibr/wiki/IMU-Noise-Model

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

once 

SCALE=25

mkdir ../cam$SCALE/; rm ../cam$SCALE/*.png; for i in *.png ; do echo convert $i -set colorspace Gray -separate -average -resize $SCALE% ../cam$SCALE/$i; convert $i -set colorspace Gray -separate -average -resize $SCALE% ../cam$SCALE/$i; done

rm dynamic.bag; rosrun kalibr kalibr_bagcreater --folder kalibr_images_dynamic/. --output-bag dynamic.bag; rosbag info dynamic.bag  

rm static.bag; rosrun kalibr kalibr_bagcreater --folder kalibr_images_static/. --output-bag static.bag ; rosbag info static.bag 

rosrun kalibr kalibr_calibrate_cameras --target april_6x6.yaml --bag static.bag --models pinhole-radtan --topics /cam25/image_raw

rosrun kalibr kalibr_calibrate_imu_camera --timeoffset-padding 1 --target april_6x6.yaml --cam "cal$SCALE""static"/static-camchain.yaml --imu imu_lsm6dsl.yaml --bag dynamic.bag
