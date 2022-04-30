# Grid Trading Backtest

What is a grid trading strategy? Simply put, we set a price range from Pa to Pb, split the price range into a number of levels, and we buy at the lower level, sell at the higher level, and repeat.

Keypoints:
1. What we get is the difference between every buy and sell orders. we profit from the bounce and back. 
2. In which situation, we profit the most? 
    - situation1: price has no trend, which means the expectation of future prices stay the same.
    - If situation1 is satisfied, we expect as much volatility as possible. If the price bounce back and force extremely, we can simply set a higer width of girds and profit from it. 
3. So, the grid trading is a trade-off between 



#### The holding position is path-dependent, so is the potential lost


Let's say, there is one stock "S" on the market. The stock "S" starts at price Pa at time t0,  ends at price Pb at time t1. **Can we calculate how much can we lost directly?**

Assume:
1. Pa, Pb is always in our grid range. 
2. Arithmetic grid. So, the grid width of one level is r


So, the average trading cost is:$$ (Pa + r + Pb) * 0.5$$; the total position size is: floor(abs(pb - pa) / r)


<!-- 2. We set the price ratio of one grid as (1+r), which means the upper grid of price Pa is (1+r)Pa
3.  -->


Assume the price follows geometric brownien motion. If there is no drift and the volatility equals \sigma, what would be the expection of grid trading returns.  








Where does the profit of Grid Trading Strategies come from? 


Let's say, there is one stock "S" on the market. The stock "S" starts at price A at time t0,  ends at price B at time t1. 