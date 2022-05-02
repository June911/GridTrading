from re import A

import numpy as np
import math

# start_price, end_price, r = 10, 14.5, 1
# start_price, end_price, r = 10, 15, 1
start_price, end_price, r = 10, 7.5, 1.2
start_price, end_price, r = 100, 150, 1


def get_grid_loss_v4(start_price, end_price, r):

    # end_price should be an array

    # position price should be a multiple of grid width r
    start_position_price = 0
    floor_end_position_price = np.floor((end_price - start_price) / r) * r
    ceil_end_position_price = np.ceil((end_price - start_price) / r) * r
    con_end_price = end_price >= start_price
    end_position_price = (
        floor_end_position_price * con_end_price
        + ceil_end_position_price * (1 - con_end_price)
    )
    sign_end_price = [1 if con else -1 for con in con_end_price]
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
    absolute_loss = get_grid_loss_v2(start_price, end_price, r)
    absolute_loss = get_grid_loss_v3(start_price, end_price, r)
    absolute_loss = get_grid_loss_v4(start_price, end_price, r)


if __name__ == "__main__":
    main()
