from price_dynamic import *
from bt_grid_trading import *
from grid_trading_loss import *
from helpful_scripts import HiddenPrints

import multiprocessing
import matplotlib.pyplot as plt
import time

inputs = {
    "X0": 10000,
    "T": 0.083,
    "mu": 0,
    "sigma": 0.6,
    "N": 100,
    "seed": 1,
    "interval_number": 100,
    # Grid trading parameters
    "r": 0.02,
    "n_grid": 4,
}

# Price dynamic
X = geometric_brownien_motion(inputs)


def bt_gt(X):
    bt = StaticGridBT(
        0,
        inputs["r"],
        inputs["n_grid"],
        "arth",
        pd.Series(X),
        is_trading_even=False,
        tx_m=0,
        tx_t=0,
        grid_quantity=0.01,
    )

    with HiddenPrints():
        bt.run_on_bar()

    final_price = X[-1]
    final_wealth = bt.wealth.iloc[-1]

    return [final_price, final_wealth]


def main():
    # record start time
    st_time = time.perf_counter()

    # init pool
    p = multiprocessing.Pool(multiprocessing.cpu_count() - 1)

    # start multiprocess
    res = p.map(bt_gt, X)
    p.close()
    p.join()

    # results
    final_prices = np.round([i[0] for i in res])
    profits = np.round([i[1] for i in res])
    profits_quantile = np.quantile(profits, [0, 0.01, 0.05, 0.1])

    df = pd.DataFrame()
    df["profits"] = profits
    df["final_prices"] = final_prices
    # df["profits_cut"] = pd.qcut(profits, 10)
    df["prices_cut"] = pd.qcut(final_prices, 10, labels=np.arange(10))
    grouped_df = df.groupby(by=["prices_cut"])

    one_grid = 2 * inputs["X0"] * inputs["r"] / inputs["n_grid"]

    df_grouped = pd.DataFrame()
    df_grouped["grouped_mean_price"] = grouped_df["final_prices"].mean()
    df_grouped["grouped_mean_profit"] = grouped_df["profits"].mean()
    df_grouped["grouped_mean_loss"] = get_grid_loss_v4(
        inputs["X0"],
        df_grouped["grouped_mean_price"].values,
        one_grid,
    )
    df_grouped["grouped_grid_quantity"] = (
        df_grouped["grouped_mean_profit"] + df_grouped["grouped_mean_loss"]
    ) / one_grid

    df_grouped.round().to_excel(os.path.join(get_results_path(), "bt_grouped.xlsx"))

    # print(df_grouped)

    # grouped_mean_price = grouped_df["final_prices"].mean()
    # grouped_mean_profit = grouped_df["profits"].mean()
    # print(grouped_mean_price.describe())
    # mean_loss = get_grid_loss_v4(inputs["X0"], grouped_mean_price.values, 0.01)

    # print(df)
    # print(2 * inputs["X0"] * inputs["r"] / inputs["n_grid"])
    # print(grouped_mean_price)
    # print(grouped_mean_profit)
    # print(mean_loss)

    print("-" * 80)
    print(f"The average profit is {np.round(np.mean(profits))}")
    print(f"The max profit is {np.max(profits)}")
    print(f"The min profit is {np.round(np.min(profits))}")
    print(f"The quantile is {profits_quantile}")
    print(f"Total time: {np.round(time.perf_counter() - st_time)} s")


if __name__ == "__main__":
    main()
