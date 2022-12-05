#!/bin/bash

PORT=8080

uvicorn main:app --port $PORT &
p1=$!

sleep 4

./tile38_v.1.30.0/tile38-1.30.0-linux-amd64/tile38-server --vv &
p2=$!

sleep 1

./tile38_v.1.30.0/tile38-1.30.0-linux-amd64/tile38-cli SETHOOK warehouse http://127.0.0.1:$PORT/endpoint NEARBY fleet FENCE WHERE timestamp 1610160257 1610160287  POINT 37.928603805154083 23.606747418144149 1000 &&

sleep 1

python ./data/set_tile38_points.py &&

sleep 15

kill $p2
kill $p1

