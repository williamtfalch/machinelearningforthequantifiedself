import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

from CreateDataset import CreateDataset
from VisualizeDataset import VisualizeDataset


class ModelBasedImputation:
    def impute_data(self, data_table):
        unimputed_data = list(map(lambda v: v[0], data_table.to_numpy()))
        not_nan_values = list(
            filter(lambda v: not np.isnan(v), unimputed_data))
        num_not_nan_values = len(not_nan_values)

        imputed_data = []
        counter = 0

        for unimputed_datapiece in unimputed_data:
            if np.isnan(unimputed_datapiece):
                imputed_value = None

                if counter == 0 or counter == num_not_nan_values - 1:
                    imputed_value = not_nan_values[counter]

                else:
                    imputed_value = (
                        not_nan_values[counter - 1] + not_nan_values[counter])/2

                imputed_data.append(imputed_value)

            else:
                imputed_data.append(unimputed_datapiece)

                if counter < num_not_nan_values - 1:
                    counter += 1

        return imputed_data


mbi = ModelBasedImputation()
dataset = CreateDataset("./", 1000)

dataset.add_numerical_dataset(
    "chapter2_result.csv", "timestamps", ["hr_watch_rate"])

imputed_data = mbi.impute_data(data_table=dataset.data_table)
