import matplotlib.pyplot as plt
import numpy as np
import pdb


def plot_iris(fname):
    header = ['Sepal width',
              'Sepal length',
              'Petal width',
              'Petal length',
              'Iris species']
    species_names = ['Iris-setosa',
                     'Iris-versicolor',
                     'Iris-virginica']

    sep_w = []  # All sepal widths
    sep_l = []  # All sepal lengths
    pet_w = []  # All petal widths
    pet_l = []  # All petal lengths

    setosa_pet_w = []  # Divide by species
    setosa_pet_l = []
    versicolor_pet_w = []
    versicolor_pet_l = []
    virginica_pet_w = []
    virginica_pet_l = []

    try:
        f = open(fname, 'r')
    except FileNotFoundError:
        raise FileNotFoundError('iris data not found')
    except Exception:
        raise Exception('Unknown error in file readout.')

    for line in f:
        info = line.rstrip().split(',')
        sep_w.append(float(info[0]))
        sep_l.append(float(info[1]))
        pet_w.append(float(info[2]))
        pet_l.append(float(info[3]))

        if (info[4] == species_names[0]):
            setosa_pet_w.append(info[2])
            setosa_pet_l.append(info[3])
        elif (info[4] == species_names[1]):
            versicolor_pet_w.append(info[2])
            versicolor_pet_l.append(info[3])
        elif (info[4] == species_names[2]):
            virginica_pet_w.append(info[2])
            virginica_pet_l.append(info[3])
        else:
            raise Exception('Iris species unrecognized.')

    data = [sep_w, sep_l, pet_w, pet_l]

    # Box plot of lengths of irises
    fig1, ax1 = plt.subplots()
    ax1.boxplot(data)
    ax1.set_xticklabels(header[:4])
    ax1.set_ylabel('cm')
    fig1.savefig('iris_boxplot.png')

    # Petal width vs length scatter plot
    fig2, ax2 = plt.subplots()
    ax2.scatter(virginica_pet_w, virginica_pet_l, label=species_names[2])
    ax2.scatter(versicolor_pet_w, versicolor_pet_l, label=species_names[1])
    ax2.scatter(setosa_pet_w, setosa_pet_l, label=species_names[0])
    ax2.xaxis.set_major_locator(plt.MaxNLocator(10))
    ax2.yaxis.set_major_locator(plt.MaxNLocator(10))
    ax2.set_xlabel('Petal width (cm)')
    ax2.set_ylabel('Petal length (cm)')
    ax2.invert_yaxis()  # It is completely unclear to me
    ax2.invert_xaxis()  # why Python is plotting this way
    ax2.legend()
    fig2.savefig('petal_width_v_length_scatter.png')

    # Multi-panel figure
    fig3, ax3 = plt.subplots(1, 2)
    ax3[0].boxplot(data)
    ax3[0].set_xticklabels(header[:4])
    ax3[0].set_ylabel('cm')
    ax3[0].spines['top'].set_visible(False)
    ax3[0].spines['right'].set_visible(False)
    ax3[0].tick_params(axis='x', rotation=45)

    ax3[1].scatter(virginica_pet_w, virginica_pet_l, label=species_names[2])
    ax3[1].scatter(versicolor_pet_w, versicolor_pet_l, label=species_names[1])
    ax3[1].scatter(setosa_pet_w, setosa_pet_l, label=species_names[0])
    ax3[1].xaxis.set_major_locator(plt.MaxNLocator(5))
    ax3[1].yaxis.set_major_locator(plt.MaxNLocator(10))
    ax3[1].set_xlabel('Petal width (cm)')
    ax3[1].set_ylabel('Petal length (cm)')
    ax3[1].invert_yaxis()  # It is completely unclear to me
    ax3[1].invert_xaxis()  # why Python is plotting this way
    ax3[1].legend()
    ax3[1].spines['top'].set_visible(False)
    ax3[1].spines['right'].set_visible(False)

    fig3.tight_layout()
    fig3.savefig('multi_panel_figure.png')
    
    print('Figures plotted and saved!')


if __name__ == '__main__':
    main()
