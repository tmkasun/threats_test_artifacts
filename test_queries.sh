#!/usr/bin/env bash

http -v --verify=no GET "https://172.16.22.1:8243/sample/1.1.1/all?wola='drop my name'" "accept: application/json" "Authorization: Bearer d9af9f24-c45f-3c82-944b-6f6d03d3108a"
 http -v --verify=no POST "https://172.16.22.1:8243/sample/1.1.1/all" "accept: application/json" "Authorization: Bearer d9af9f24-c45f-3c82-944b-6f6d03d3108a" "@./json/sql_injection.json