from numpy import mean, std
from matplotlib import pyplot as plt
import pandas as pd

from CreateDataset import CreateDataset
from OutlierDetection import DistributionBasedOutlierDetection, DistanceBasedOutlierDetection
from VisualizeDataset import VisualizeDataset

dataset = CreateDataset("./", 1000)
distribution_bod = DistributionBasedOutlierDetection()
distance_bod = DistanceBasedOutlierDetection()
vis = VisualizeDataset()

dataset.add_numerical_dataset(
    "chapter2_result.csv", "timestamps", ["acc_phone_x"])

chauvs = {}
mixes = {}
simples = {}
localoutliers = {}

data_table = dataset.data_table

for i in range(5):
    c = 1 + i*0.5
    chauvs[i] = distribution_bod.chauvenet(data_table, "acc_phone_x", c=c)
    mixes[i] = distribution_bod.mixture_model(data_table, "acc_phone_x")

    simples[i] = distance_bod.simple_distance_based(
        data_table, ["acc_phone_x"], "euclidean", c, 1/c)
    localoutliers[i] = distance_bod.local_outlier_factor(
        data_table, ["acc_phone_x"], "euclidean", 2*c)

    # vis.plot_dataset(chauvs[i], ["x"])

    # heart_rates = list(map(lambda v: (v[0], v[1]), list(pd.read_csv(
    #    "../crowdsignals/heart_rate_smartwatch.csv", usecols=[2, 3]).values)))
