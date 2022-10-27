import data_processor as proc
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_file_name', type=str, required=True)
    parser.add_argument('--num_rows', type=int, required=True)
    parser.add_argument('--num_cols', type=int, required=True)

    args = parser.parse_args()
    proc.write_matrix_to_file(args.num_rows,
                              args.num_cols,
                              args.data_file_name)


if __name__ == '__main__':
    main()
