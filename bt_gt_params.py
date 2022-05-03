from price_dynamic import *
from bt_grid_trading import *
from grid_trading_loss import *
from helpful_scripts import *

import matplotlib.pyplot as plt

# Monte Carlo Simulation
inputs = {
    "X0": 10000,
    "T": 1,
    "mu": 0,
    "sigma": 0.2,
    "N": 10,
    "seed": 1,
    "interval_number": 100,
    # Grid trading parameters
    "r": 0.1,
    "n_grid": 100,
}


def bt_gt(inputs):
    # Price dynamic
    X = geometric_brownien_motion(inputs)

    # Backtest Grid Trading
    profits = np.zeros(X.shape[0])
    for i in range(X.shape[0]):
        bt = StaticGridBT(
            0,
            inputs["r"],
            inputs["n_grid"],
            "arth",
            pd.Series(X[i, :]),
            is_trading_even=False,
            tx_m=0,
            tx_t=0,
            grid_quantity=0.01,
        )

        with HiddenPrints():
            bt.run_on_bar()
        profits[i] = bt.wealth.iloc[-1]

    # print(f"final profits: {profits}")
    print(f"final avg profits: {np.mean(profits)}")
    return profits


def main():
    # test params

    # 1. N
    #   -> to see if the expected strategy profit converge
    lst_N = [10, 50, 100, 500, 1000, 2000, 4000, 6000, 8000, 10000]
    lst_avg_profit = []
    for N in lst_N:
        print("-" * 80)
        print(f"current N: {N}")

        inputs["N"] = N
        profits = bt_gt(inputs)
        avg_profits = np.mean(profits)
        lst_avg_profit.append(avg_profits)

    df_res = pd.DataFrame()
    df_res["N"] = lst_N
    df_res["avg_profit"] = lst_avg_profit
    df_res.to_excel(os.path.join(get_results_path(), "bt_N.xlsx"))

    # 2. number of time interval
    lst_interval = [10, 50, 100, 500, 1000]
    inputs["N"] = 1000
    lst_avg_profit = []
    for interval_number in lst_interval:
        print("-" * 80)
        print(f"current interval number : {interval_number}")

        inputs["interval_number"] = interval_number
        profits = bt_gt(inputs)
        avg_profits = np.mean(profits)
        lst_avg_profit.append(avg_profits)

    df_res = pd.DataFrame()
    df_res["interval_number"] = lst_interval
    df_res["avg_profit"] = lst_avg_profit
    df_res.to_excel(os.path.join(get_results_path(), "bt_interval_number.xlsx"))

    # 3. number of grid
    lst_inputs = [10, 20, 50, 100]
    inputs["interval_number"] = 100
    lst_avg_profit = []
    for i in lst_inputs:
        print("-" * 80)
        print(f"current n_grid : {i}")

        inputs["n_grid"] = i
        profits = bt_gt(inputs)
        avg_profits = np.mean(profits)
        lst_avg_profit.append(avg_profits)

    df_res = pd.DataFrame()
    df_res["n_grid"] = lst_inputs
    df_res["avg_profit"] = lst_avg_profit
    df_res.to_excel(os.path.join(get_results_path(), "bt_n_grid.xlsx"))

    # 4. sigma
    lst_inputs = [0.01, 0.05, 0.1, 0.2, 0.5]
    inputs["n_grid"] = 100
    lst_avg_profit = []
    for i in lst_inputs:
        print("-" * 80)
        print(f"current interval number : {i}")

        inputs["sigma"] = i
        profits = bt_gt(inputs)
        avg_profits = np.mean(profits)
        lst_avg_profit.append(avg_profits)

    df_res = pd.DataFrame()
    df_res["sigma"] = lst_inputs
    df_res["avg_profit"] = lst_avg_profit
    df_res.to_excel(os.path.join(get_results_path(), "bt_sigma.xlsx"))

    # 5. r
    lst_inputs = [0.1, 0.2, 0.3]
    inputs["sigma"] = 0.1
    lst_avg_profit = []
    for i in lst_inputs:
        print("-" * 80)
        print(f"current interval number : {i}")

        inputs["r"] = i
        profits = bt_gt(inputs)
        avg_profits = np.mean(profits)
        lst_avg_profit.append(avg_profits)

    df_res = pd.DataFrame()
    df_res["r"] = lst_inputs
    df_res["avg_profit"] = lst_avg_profit
    df_res.to_excel(os.path.join(get_results_path(), "bt_r.xlsx"))


if __name__ == "__main__":
    main()
