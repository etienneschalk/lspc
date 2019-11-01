#!/bin/sh

# This script should be launched from the main folder of the project:
# $ ./scripts/run_tests.sh

echo "/------------------------------------\\"
echo "| Creating test folders and files... |"
echo "\\------------------------------------/"
./scripts/make_test_folders.sh

echo ""
echo "/-----------------------\\"
echo "| Running unit tests... |"
echo "\\-----------------------/"
python3 -m unittest discover -s test/unit -v

echo ""
echo "/------------------------------\\"
echo "| Running integration tests... |"
echo "\\------------------------------/"
python3 -m unittest discover -s test/integration -v
