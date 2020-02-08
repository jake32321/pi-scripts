#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"
nohup python3 $1 >/dev/null 2>&1 &