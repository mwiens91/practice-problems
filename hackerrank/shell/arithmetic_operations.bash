#!/usr/bin/env bash

read eqn_string
printf "%.3f\n" $(echo $eqn_string | bc -l)
