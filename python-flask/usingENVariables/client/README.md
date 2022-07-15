podman build -t envapp .

podman run -d --network=flask -e URL=http://flaskapi:5000 -p 20000:20000 localhost/envapp