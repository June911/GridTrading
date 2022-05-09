from multiprocessing import Pool
import pandas as pd

data_table = None
# data_table = pd.DataFrame()
# data_table.loc[:, "x"] = [1, 2, 3]
# data_table.loc[:, "y"] = [4, 5, 6]


def init_data_table(my_data_table=[], *args):
    global data_table
    data_table = my_data_table


def process_data(index):
    # create data processor object and run cpu intensive task here
    # print(type(data_table.loc[index, "x"]))
    return str(index) + " ++++ " + str(data_table.loc[index, "x"])


def main():
    # call db functions once and get data table from db
    data_table = pd.DataFrame()
    data_table.loc[:, "x"] = [1, 2, 3]
    data_table.loc[:, "y"] = [4, 5, 6]
    # print(process_data(1))

    pool = Pool(processes=2, initializer=init_data_table, initargs=(data_table,))
    x = pool.map(process_data, range(2))
    print(x)


if __name__ == "__main__":
    main()
