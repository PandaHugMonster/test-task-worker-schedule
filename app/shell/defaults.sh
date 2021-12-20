#!/usr/bin/env bash

_HOST="localhost";
_PORT="8005";

_OP_USER="root";
_OP_PASS="root";

_WORKER_NAME='Jane Doe';
_WORKER_BIRTHDATE='1980-01-01';

_WORKERS_URL="http://${_HOST}:${_PORT}/workers";

_ID=$(
  curl -s -H 'Accept: application/json; indent=4' -u ${_OP_USER}:${_OP_PASS} \
    "${_WORKERS_URL}/" -X POST \
    -d "name=${_WORKER_NAME}&birthdate=${_WORKER_BIRTHDATE}" | jq '.id' 2> /dev/null
);

if [ -n "${_ID}" ]; then
  echo -ne "Created user with id: ${_ID}\n";
  echo -ne "Creating shifts\n";

  _WORKER=$(echo "${_WORKERS_URL}/${_ID}/" | jq -sRr @uri);
  _URL="http://${_HOST}:${_PORT}/shifts/";

  for _I in 1 2 3 4; do
    curl -s -H 'Accept: application/json; indent=4' -u ${_OP_USER}:${_OP_PASS} \
        "${_URL}" -X POST \
        -d "worker=${_WORKER}&memo=AUTO${_I}&target_dt=2021-12-0${_I}T00:00";
  done;

fi;