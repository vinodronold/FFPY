#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER fivefrets WITH password '$POSTGRES_PASSWORD';
    CREATE DATABASE fivefrets;
    GRANT ALL PRIVILEGES ON DATABASE fivefrets TO fivefrets;
EOSQL
