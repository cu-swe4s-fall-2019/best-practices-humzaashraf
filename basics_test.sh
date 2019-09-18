test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest


# Test the code format fits the PEP8 style guidelines
run style_test pycodestyle style.py
assert_no_stdout
assert_exit_code 0

run col_stats_test pycodestyle get_column_stats.py
assert_no_stdout
assert_exit_code 0



(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

python get_column_stats.py data.txt 2


V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

python get_column_stats.py data.txt 2
