#!/usr/bin/env bash

tail -n +2 | tr " " "\n" | sort -n | uniq -u
