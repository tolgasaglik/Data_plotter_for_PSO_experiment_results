import numpy as np
import matplotlib.pyplot as plt
import os


def main():
    folder_names = ["sphere", "griewank", "rosenbrock", "schaffer", "rastrigin", "schwefel", "ackley", "himmelblau"]
    folder_names = ['schaffer']
    for folder in folder_names:
        lozi_file = None
        logistic_file = None
        if folder is 'ackley':
            lozi_file = "/lozi_15_-02.dat"
            logistic_file = "/logistic_400.dat"
        elif folder is 'schwefel':
            lozi_file = "/lozi_15_045.dat"
            logistic_file = "/logistic_395.dat"
        elif folder is 'schaffer':
            lozi_file = "/lozi_18_010.dat"
            logistic_file = "/logistic_375.dat"

        legend_list = []

        #Basic
        basic_data = np.genfromtxt("logistic_experiment_results/" + folder + "/logistic_basic.dat")
        gen = np.arange(len(basic_data.mean(axis=1)))
        plt.plot(gen, basic_data.mean(axis=1), '-')
        legend_list.append('Basic PSO')

        #Rossler
        rossler_data = np.random.rand(3500, 0)
        experiment_names = []
        for i in range(1, 16):
            experiment_names.append('r' + str(i))
        for i in range(5):
            temp_data = np.genfromtxt(
                "/Users/tolgasaglik/Desktop/ROSSLER/%s/output/%s/rossler_results.dat" % (experiment_names[i+10], folder))
            rossler_data = np.c_[rossler_data, temp_data]
        plt.plot(gen, rossler_data.mean(axis=1),'-')
        legend_list.append('Rossler PSO')

        #Lorenz
        lorenz_data = np.genfromtxt("lorenz_experiment_results/"+folder+"/lorenz_results.dat")
        plt.plot(gen, lorenz_data.mean(axis=1),'-')
        legend_list.append('Lorenz PSO')

        #Lozi

        lozi_data = np.genfromtxt("lozi_experiment_results/" + folder + lozi_file)
        plt.plot(gen, lozi_data, '-')
        legend_list.append('Lozi PSO')

        # Logistic
        logistic_data = np.genfromtxt("logistic_experiment_results/" + folder + logistic_file)
        plt.plot(gen, logistic_data.mean(axis=1), '-')
        legend_list.append('Logistic PSO')
        plt.title(folder.swapcase())
        plt.xlabel("Generation")
        plt.ylabel("Minimum Fitness")
        plt.legend(legend_list, loc='upper right')
        #plt.show()
        plt.savefig('./plots/all_' + folder + '.png', dpi=500)
        plt.clf()


if __name__ == '__main__':
    main()