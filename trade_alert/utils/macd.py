"""
Helper functions/classes to generate MACD plots given a certain length of time.
"""
import pandas_ta as ta


def calculate_macd(
    ticker_df,
    fast:int=12,
    slow:int=26,
    signal:int=9
    ):
    """
    Calculate the Moving Average Convergence Divergence (MACD) of a given stock.
    NOTE: Still need to do tests when 2+ stocks are included in the dataframe

    """
    # Using the pandas_ta library
    return ticker_df.ta.macd(
        close='close',
        fast=fast,
        slow=slow,
        signal=signal,
        append=True
    )
