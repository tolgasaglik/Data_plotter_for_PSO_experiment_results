import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import style


def main():
    folder_names = ["sphere", "griewank", "rosenbrock", "schaffer", "rastrigin", "schwefel", "ackley", "himmelblau"]
    #folder_names = ["schwefel", "griewank"]
#    colors = ['r-', 'g-', 'b-', 'y-', '-']
    experiment_names = []
    for i in range(1,16):
        experiment_names.append('r'+str(i))

    for problem in folder_names:
        Rossler_1 = np.random.rand(3500, 0)
        Rossler_2 = np.random.rand(3500, 0)
        Rossler_3 = np.random.rand(3500, 0)
        for i in range(5):
            temp_data1 = np.genfromtxt(
                "/Users/tolgasaglik/Desktop/ROSSLER/%s/output/%s/rossler_results.dat" % (experiment_names[i], problem))
            temp_data2 = np.genfromtxt(
                "/Users/tolgasaglik/Desktop/ROSSLER/%s/output/%s/rossler_results.dat" % (experiment_names[i+5], problem))
            temp_data3 = np.genfromtxt(
                "/Users/tolgasaglik/Desktop/ROSSLER/%s/output/%s/rossler_results.dat" % (experiment_names[i+10], problem))
            Rossler_1 = np.c_[Rossler_1, temp_data1]
            Rossler_2 = np.c_[Rossler_2, temp_data2]
            #if i is not 3:
            Rossler_3 = np.c_[Rossler_3, temp_data3]
        basic_data = np.genfromtxt("logistic_experiment_results/" + problem + "/logistic_basic.dat")
        gen = np.arange(len(basic_data.mean(axis=1)))
        plt.plot(gen, Rossler_1.mean(axis=1), '-')
        plt.plot(gen, Rossler_3.mean(axis=1), '-')
        plt.plot(gen, Rossler_2.mean(axis=1), '-')
        plt.plot(gen, basic_data.mean(axis=1), '-')
        plt.title(problem.swapcase())
        plt.xlabel("Generation")
        plt.ylabel("Minimum Fitness")
        alpha = u'\u03B1'
        legend_list=[alpha+' = -0.25',alpha+' = 0.78',alpha+' = 1.135','basic']
        plt.legend(legend_list, loc = 'upper right')
        plt.savefig('./plots/rossler_' + problem + '_plot.png', dpi=500)
        #plt.show()
        plt.clf()


if __name__ == '__main__':
    main()
