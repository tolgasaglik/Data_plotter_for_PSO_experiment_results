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
#/Users/tolgasaglik/Desktop/ROSSLER/r1/output/ackley/rossler_result.dat
    # for folder in folder_names:
    #     directory = os.fsencode("rossler_experiment_results/"+folder)
    #     data = []
    #     i = 0
    #     legend_list = []
    #     for file in os.listdir(directory):
    #         filename = os.fsdecode(file)
    #         if filename[0] is not '.': # ignore certain files
    #             temp_data = np.genfromtxt("rossler_experiment_results/" + folder + "/" + filename)
    #             if temp_data[3000] is not "nan" or temp_data[10] < temp_data[3000]:
    #                 legend_list.append(filename[9:len(filename)-4])
    #                 data.append(temp_data)
    #                 gen = np.arange(3500)
    #                 plt.plot(gen, data[i], '-')
    #                 i += 1
    #     plt.title(folder.swapcase())
    #     plt.xlabel("Generation")
    #     plt.ylabel("Minimum Fitness")
    #     plt.legend(legend_list, loc='upper right')
    #     plt.savefig('plots/rossler_' + folder + '.png', dpi=500)
    #     # plt.show()
    #     plt.clf()

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
            Rossler_3 = np.c_[Rossler_3, temp_data3]
        basic_data = np.genfromtxt("lozi_experiment_results/" + problem + "/lozi_basic.dat")
        gen = np.arange(len(basic_data.mean(axis=1)))
        plt.plot(gen, Rossler_1.mean(axis=1), '-')
        plt.plot(gen, Rossler_2.mean(axis=1), '-')
        plt.plot(gen, Rossler_3.mean(axis=1), '-')
        plt.plot(gen, basic_data.mean(axis=1), '-')
        plt.title(problem.swapcase())
        plt.xlabel("Generation")
        plt.ylabel("Minimum Fitness")
        legend_list=['alpha = -0.25','alpha = 0.78','alpha =1.135','basic']
        plt.legend(legend_list, loc = 'upper right')
        plt.savefig('./plots/rossler_' + problem + '_plot.png', dpi=500)
        #plt.show()
        plt.clf()


if __name__ == '__main__':
    main()
