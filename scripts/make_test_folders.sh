#!/bin/sh

# This script should be launched from the main folder of the project
# (when running `run_tests.sh` script)

# Creates sample directory
rm -rf sample
mkdir sample
cd sample
pwd
mkdir \
  dir0 \
  dir1 \
  dir2 \
  dir1/dir1_A \
  dir2/dir2_A \
  dir2/dir2_B \
  .dirhidden
touch \
   file0 \
   dir1/dir1_file0 \
   dir1/.dir1_filehidden \
   dir2/dir2_A/dir2_A_file0 \
   dir2/dir2_A/dir2_A_file1 \
   dir2/dir2_B/dir2_B_filebig \
   .dirhidden/.dirhidden_filehidden
echo "0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n" >> file0
echo "0" >> dir1/dir1_file0
echo "01234567" >> dir2/dir2_A/dir2_A_file0
echo "01234567\n01234567" >> dir2/dir2_A/dir2_A_file1
head -c 10241024 < /dev/urandom > dir2/dir2_B/dir2_B_filebig
echo "\nlines\t words\t bytes\t   file"
wc  \
   file0 \
   dir1/dir1_file0 \
   dir1/.dir1_filehidden \
   dir2/dir2_A/dir2_A_file0 \
   dir2/dir2_A/dir2_A_file1 \
   dir2/dir2_B/dir2_B_filebig \
   .dirhidden/.dirhidden_filehidden

tree -a
