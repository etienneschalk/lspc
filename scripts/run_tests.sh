#!/bin/sh

# This script should be launched from the main folder of the project:
# $ ./scripts/run_tests.sh

echo "/--------------------------\\"
echo "| Creating test folders... |"
echo "\\--------------------------/"
./scripts/make_test_folders.sh

echo ""
echo "/------------------\\"
echo "| Running tests... |"
echo "\\------------------/"
python3 -m unittest -v
