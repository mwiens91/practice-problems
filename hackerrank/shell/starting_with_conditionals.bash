#!/usr/bin/env bash
read x

case $x in
y | Y)
    echo YES;;
n | N)
    echo NO;;
*)
    echo WOOPS;;
esac
