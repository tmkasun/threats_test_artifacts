#!/usr/bin/env bash

http -v --verify=no  POST "https://172.16.22.1:8243/dynamicep/1.1.1/sample" "accept: application/json" "Content-Type: application/json" "Authorization: Bearer 14ddbbaf-d7a2-3861-9ebc-d0d4b0cf35a6" operation=menua