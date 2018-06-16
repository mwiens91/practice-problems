#!/usr/bin/env python3

from bisect import bisect_left
from math import ceil
import re
import sys


def find_next_bus_stop_index(coord):
    """Find the next bus stop index.

    If the coordinate passed in matches a bus stop coordinate, the index
    of this bus stop is passed in, not the next bus stop after it.
    """
    global num_bus_stops, bus_stops
    return bisect_left(bus_stops, coord, 0, num_bus_stops)

def find_waiting_time(init_time, position):
    """Find how long you need to wait for a bus.

    This is with respect to a time and position.
    """
    global bus_period, bus_speed
    return (ceil((init_time - position/bus_speed)/ bus_period)
            * bus_period + position/bus_speed - init_time)


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
num_bus_stops = int(lines[0])
bus_stops = [int(i) for i in re.split(r'\D', lines[1])]
bus_period, bus_speed = [int(i) for i in re.split(r'\D', lines[2])]
num_people = int(lines[3])
people = [[int(i) for i in re.split(r'\D', line)] for line in lines[4:]]

# For each bus stop compute how long the bus takes to get to the end
end_location = bus_stops[-1]
bus_journey_times_per_stop = [(end_location - x)/bus_speed for x in bus_stops]

# Solve the problem for each person
for person in people:
    # Unpack variables
    person_pos, initial_time, person_speed = person

    # Find worst case walking time
    walking_time = (end_location - person_pos) / person_speed

    # If the person is faster than the bus, just print the walking time
    if person_speed >= bus_speed:
        print(walking_time + initial_time)
        continue

    # Find all of the bus stops we need to consider
    next_bus_stop_index = find_next_bus_stop_index(person_pos)

    if bus_stops[next_bus_stop_index] == person_pos:
        # We start at a bus stop, only consider that one
        bus_stop_indices = [next_bus_stop_index]
    else:
        # Consider the bus stop to the right *and* left
        bus_stop_indices = [next_bus_stop_index,
                            next_bus_stop_index - 1]

    # Find the time it takes if we wait at the bus stops
    bus_times = []

    for bus_stop_index in bus_stop_indices:
        # Get bus position
        bus_position = bus_stops[bus_stop_index]

        # Find the time
        time_to_walk_to_stop = abs(bus_position - person_pos) / person_speed
        time_to_wait_at_stop = find_waiting_time(
            initial_time + time_to_walk_to_stop,
            bus_position)

        bus_times.append(time_to_walk_to_stop
                         + time_to_wait_at_stop
                         + bus_journey_times_per_stop[bus_stop_index])

    # Print the minimum time
    minimum_time = min(bus_times + [walking_time]) + initial_time
    print(minimum_time)
