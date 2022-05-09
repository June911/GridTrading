import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import os

from torch import sign

from helpful_scripts import get_results_path

# start_price, end_price, r = 10, 14.5, 1
# start_price, end_price, r = 10, 15, 1
# start_price, end_price, r = 10, 7.5, 1.2
start_price, end_price, r = 10000, 15000, 1

ary = np.array([0.001, 0.01])
ary = np.append(ary, (np.arange(0.1, 1, 0.1)))
end_price_array = np.sort(np.append(-ary, ary) * start_price) + start_price
# print(end_price_array)


def get_grid_loss_v4(start_price, end_price, r):

    # end_price should be an array
    # position price should be a multiple of grid width r
    floor_end_position_price = np.floor((end_price - start_price) / r) * r
    ceil_end_position_price = np.ceil((end_price - start_price) / r) * r
    con_end_price = end_price >= start_price
    end_position_price = (
        floor_end_position_price * con_end_price
        + ceil_end_position_price * (1 - con_end_price)
    )
    sign_end_price = np.array([1 if con else -1 for con in con_end_price])
    average_position_price = (r * sign_end_price + end_position_price) * 0.5

    # if end_price >= start_price:
    #     end_position_price = np.floor((end_price - start_price) / r) * r
    #     average_position_price = (r + end_position_price) * 0.5
    # else:
    #     print(1)
    #     end_position_price = np.ceil((end_price - start_price) / r) * r
    #     average_position_price = (-r + end_position_price) * 0.5

    position_size = np.floor((end_position_price) / r)
    absolute_loss = (end_price - start_price - average_position_price) * position_size

    # print(start_position_price, end_position_price)
    # print(average_position_price, position_size, absolute_loss)

    return absolute_loss


def get_grid_loss_v3(start_price, end_price, r):

    # position price should be a multiple of grid width r
    start_position_price = 0
    if end_price >= start_price:
        end_position_price = np.floor((end_price - start_price) / r) * r
        average_position_price = (r + end_position_price) * 0.5
    else:
        end_position_price = np.ceil((end_price - start_price) / r) * r
        average_position_price = (-r + end_position_price) * 0.5

    position_size = np.floor((end_position_price) / r)
    absolute_loss = (end_price - start_price - average_position_price) * position_size

    # print(start_position_price, end_position_price)
    # print(average_position_price, position_size, absolute_loss)

    return absolute_loss


def get_grid_loss_v2(start_price, end_price, r):

    # position price should be a multiple of grid width r
    start_position_price = 0
    if end_price >= start_price:
        end_position_price = math.floor((end_price - start_price) / r) * r
        average_position_price = (r + end_position_price) * 0.5
    else:
        print(1)
        end_position_price = math.ceil((end_price - start_price) / r) * r
        average_position_price = (-r + end_position_price) * 0.5

    position_size = math.floor((end_position_price - start_position_price) / r)
    absolute_loss = (end_price - start_price - average_position_price) * position_size

    print(start_position_price, end_position_price)
    print(average_position_price, position_size, absolute_loss)

    return absolute_loss


def get_grid_loss_v1(start_price, end_price, r):

    # position price should be a multiple of grid width r
    if end_price >= start_price:
        start_position_price = math.floor(start_price / r) * r
        end_position_price = math.floor(end_price / r) * r
        average_position_price = (start_position_price + r + end_position_price) * 0.5
    else:
        start_position_price = math.ceil(start_price / r) * r
        end_position_price = math.ceil(end_price / r) * r
        average_position_price = (start_position_price - r + end_position_price) * 0.5

    # average_position_price = (start_position_price + r + end_position_price) * 0.5
    position_size = math.floor((end_position_price - start_position_price) / r)
    absolute_loss = (end_price - average_position_price) * position_size
    print(start_position_price, end_position_price)
    print(average_position_price, position_size, absolute_loss)
    return absolute_loss


def main():
    # absolute_loss = get_grid_loss_v2(start_price, end_price, r)
    absolute_loss = get_grid_loss_v3(start_price, end_price, r)
    print(absolute_loss)
    absolute_loss = get_grid_loss_v4(start_price, end_price_array, r)
    print(absolute_loss)

    plt.figure()
    plt.plot(end_price_array, absolute_loss)
    plt.show()

    df_res = pd.DataFrame()
    df_res["end_price_array"] = end_price_array
    df_res["absolute_loss"] = absolute_loss
    df_res.to_excel(os.path.join(get_results_path(), "absolute_loss.xlsx"))
    print(df_res)


if __name__ == "__main__":
    main()
