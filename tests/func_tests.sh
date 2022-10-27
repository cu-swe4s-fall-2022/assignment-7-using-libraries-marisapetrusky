test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_use_plotter python use_plotter.py --data_file_name 'iris.data'
assert_exit_code 0

run test_use_data_proc_good python use_data_processor.py --data_file_name 'test_matrix.csv' --num_rows 15 --num_cols 15 
assert_in_stdout 'successfully'
assert_exit_code 0

run test_use_plotter python use_plotter.py --data_file_name 'iris.data'
assert_in_stdout 'plotted'
assert_exit_code 0
