podman build -t envapp .
podman run -d --network=flask -e URL=http://flaskapi:5000 -p 10000:10000 localhost/envapp