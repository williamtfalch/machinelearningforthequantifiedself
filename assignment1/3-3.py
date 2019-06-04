from numpy import mean, std
from matplotlib import pyplot as plt
import pandas as pd

from CreateDataset import CreateDataset
from OutlierDetection import DistributionBasedOutlierDetection, DistanceBasedOutlierDetection
from VisualizeDataset import VisualizeDataset

acc_x_dataset = CreateDataset("../crowdsignals/", 1000)
dbod = DistributionBasedOutlierDetection()
vis = VisualizeDataset()

acc_x_dataset.add_numerical_dataset(
    "accelerometer_phone_tiny.csv", "timestamps", ["x"])


chauvs = {}
for i in range(5):
    c = 1 + i*0.5
    chauvs[i] = dbod.chauvenet(acc_x_dataset.data_table, "x", c=c)
    # print(chauvs[i])
    vis.plot_dataset(chauvs[i], ["x"])


# heart_rates = list(map(lambda v: (v[0], v[1]), list(pd.read_csv(
#    "../crowdsignals/heart_rate_smartwatch.csv", usecols=[2, 3]).values)))
