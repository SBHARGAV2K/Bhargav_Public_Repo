import numpy as np
import pandas as pd

class MovingAverage:
    def __init__(self, window_size):
        self.window_size = window_size

    def apply(self, sensor_data):
        """
        Apply moving average filter to the sensor data.

        :param sensor_data: The sensor data to be filtered.
        :type sensor_data: pandas.DataFrame
        
        :return: Filtered data after applying the moving average.
        :type: pandas.DataFrame
        """
        try:
            # Ensure the window size is a positive integer
            if not isinstance(self.window_size, int) or self.window_size <= 0:
                raise ValueError(
                     "Window size must be a positive integer."
                )
            
            # Apply the moving average filter
            clean_ride_data = sensor_data.copy()
            
            for column in sensor_data.columns:
                if column not in [
                        
                    ]:
                    # Apply moving average to each sensor data column
                    # Using rolling mean with specified window size
                    clean_ride_data[f"{column}_filt"] = sensor_data[column].rolling(window=self.window_size).mean()
            
            # Reset index to maintain the original DataFrame structure
            clean_ride_data.bfill(inplace=True)  # Backfill to handle NaN values at the start
            clean_ride_data.reset_index(drop=True, inplace=True)
            
            return clean_ride_data
        
        except Exception as e:
            raise Exception(
                f"Error applying moving average filter: {e}"
            )