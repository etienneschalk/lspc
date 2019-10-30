#!/bin/sh

# creates sample directory
mkdir sample
cd sample
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
   dir2/dir2_B/dir2_A_filebig \
   .dirhidden/.dirhidden_filehidden
echo "0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n" >> file0
echo "0" >> dir1/dir1_file0
echo "01234567" >> dir2/dir2_A/dir2_A_file0
echo "01234567\n01234567" >> dir2/dir2_A/dir2_A_file1
head -c 10241024 < /dev/urandom > dir2/dir2_B/dir2_A_filebig
echo "\nlines words bytes file"
wc  \
   file0 \
   dir1/.dir1_filehidden \
   dir1/dir1_file0 \
   dir2/dir2_A/dir2_A_file0 \
   dir2/dir2_A/dir2_A_file1

tree -a
