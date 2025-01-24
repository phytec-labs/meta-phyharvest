#!/bin/bash

# Main loop
m=0.000229   # Constant value
b=-1995.8    # Changed back to -1987.8

# Read values
value0=$(cat /sys/bus/iio/devices/iio:device0/in_voltage0_raw 2>/dev/null)
value1=$(cat /sys/bus/iio/devices/iio:device0/in_voltage1_raw 2>/dev/null)

# Verify both values are numeric
if [[ -z "$value0" || -z "$value1" || ! "$value0" =~ ^[0-9]+$ || ! "$value1" =~ ^[0-9]+$ ]]; then
    echo "Error: Invalid or missing voltage data."
    exit 1
fi

# Store values in the array
valAvg=$(( ($value0 + $value1) / 2 ))

# Calculate the final result by multiplying the average by m, rounding, and then adding b
result=$(echo "scale=10; $valAvg * $m + $b" | bc)
result_rounded=$(printf "%.0f" "$result")  # Round to the nearest integer

# Check if the weight is negative or less than 1
if (( $(echo "$result_rounded < 1" | bc -l) )); then
    result_rounded=0
fi

echo $result_rounded

