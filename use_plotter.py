import plotter as plot
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_file_name', type=str, required=True)

    args = parser.parse_args()
    plot.plot_iris(args.data_file_name)


if __name__ == '__main__':
    main()
