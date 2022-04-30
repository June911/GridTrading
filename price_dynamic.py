import numpy as np
import time

inputs = {
    "X0": 100,
    "T": 1,
    "mu": 0,
    "sigma": 0.01,
    "N": 1000,
    "seed": 1,
    "interval_number": 100,
}


def geometric_brownien_motion(inputs):
    """monte carlo simulation of geometric brownien motion

    Args:
        inputs (_type_): _description_
    """
    # Read inputs
    X0 = inputs["X0"]
    T = inputs["T"]
    mu = inputs["mu"]
    sigma = inputs["sigma"]
    seed = inputs["seed"]
    N = int(inputs["N"])
    d = int(inputs["interval_number"])
    dt = T / d

    debut = time.perf_counter()

    # Initialize seed
    if not np.isnan(seed):
        np.random.seed(int(seed))

    # Calculate drift
    drift = (mu - 0.5 * sigma**2) * dt

    # Calculate diffusion
    diffusion = sigma * dt**0.5

    # Generate random variables
    z = np.random.normal(size=(N, d))

    # Simulate the underlying asset's trajectory
    delta_X = np.exp(drift + diffusion * z)

    X = np.concatenate((np.ones((N, 1)) * X0, delta_X), axis=1)
    X = np.cumprod(X, axis=1)
    # print(np.mean(X[:, -1]))

    return X


def main():
    geometric_brownien_motion(inputs)


if __name__ == "__main__":
    main()
