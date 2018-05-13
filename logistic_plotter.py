import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import style


# style.use("fivethirtyeight")
def main():
    folder_names = ["sphere", "griewank", "rosenbrock", "schaffer", "rastrigin", "schwefel", "ackley", "himmelblau"]
    #folder_names = ["griewank", "rastrigin"]
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
        legend_list = []
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename[0] is not '.':
                if filename[9] is "b":  # ignore certain files
                    print(filename)
                    temp_data = np.genfromtxt("logistic_experiment_results/" + folder + "/" + filename)
                    if not np.isnan(temp_data).any():
                        average = np.average(temp_data, axis=1)
                        if average[10] > average[3000]:
                            legend_list.append(filename[9:len(filename) - 4])
                            gen = np.arange(len(average))
                            plt.plot(gen, average, '-')
                elif int(filename[9:11]) > 36: # ignore certain files
                    print(filename)
                    temp_data = np.genfromtxt("logistic_experiment_results/" + folder + "/" + filename)
                    if not np.isnan(temp_data).any():
                        average = np.average(temp_data, axis=1)
                        if average[10] > average[3000]:
                            legend_list.append(filename[9:len(filename)-4])
                            gen = np.arange(len(average))
                            plt.plot(gen, average, '-')
        plt.title(folder.swapcase())
        plt.xlabel("Generation")
        plt.ylabel("Minimum Fitness")
        plt.legend(legend_list, loc='upper right')
        plt.savefig('plots/logistic_' + folder + '.png', dpi=500)
        #plt.show()
        plt.clf()


if __name__ == '__main__':
    main()
