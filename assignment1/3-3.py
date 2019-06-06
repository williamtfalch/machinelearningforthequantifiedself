from numpy import mean, std
from matplotlib import pyplot as plt
import pandas as pd

from CreateDataset import CreateDataset
from VisualizeDataset import VisualizeDataset

dataset = CreateDataset("./", 1000)
vis = VisualizeDataset()

dataset.add_numerical_dataset(
    "chapter2_result.csv", "timestamps", ["hr_watch_rate"])

data_table = dataset.data_table
