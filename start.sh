docker_id=$(docker run --privileged --env-file .env -d tfindelkind/iot-pi)
export docker_id