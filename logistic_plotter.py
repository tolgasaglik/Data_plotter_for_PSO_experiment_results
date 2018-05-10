import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import style


# style.use("fivethirtyeight")
def main():
    folder_names = ["sphere", "griewank", "rosenbrock", "schaffer", "rastrigin", "schwefel", "ackley", "himmelblau"]
    #folder_names = ["schwefel"]
    #file_names = ["basic", "logistic", "lozi", "lorenz", "rossler"]
#    colors = ['r-', 'g-', 'b-', 'y-', '-']
    #data = [None] * len(file_names)

    # fig = plt.figure()
    # ax_list = [fig.add_subplot(231),
    #            fig.add_subplot(232),
    #            fig.add_subplot(233),
    #            fig.add_subplot(234),
    #            fig.add_subplot(235)]

    for folder in folder_names:
        directory = os.fsencode("logistic_experiment_results/"+folder)
        data = []
        i = 0
        legend_list = []
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename[0] is not '.' and filename[11] is not '5' and filename[10] is not '7': # ignore certain files
                temp_data = np.genfromtxt("logistic_experiment_results/" + folder + "/" + filename)
                if not np.isnan(temp_data).any() or temp_data[10][0] < temp_data[3000][0]:
                    legend_list.append(filename[9:len(filename)-4])
                    data.append(temp_data)
                    gen = np.arange(3500)
                    plt.plot(gen, data[i], '-')
                    i += 1
        plt.title(folder.swapcase())
        plt.xlabel("Generation")
        plt.ylabel("Minimum Fitness")
        plt.legend(legend_list, loc='upper right')
        plt.savefig('plots/logistic_' + folder + '.png', dpi=500)
        # plt.show()
        plt.clf()


if __name__ == '__main__':
    main()
