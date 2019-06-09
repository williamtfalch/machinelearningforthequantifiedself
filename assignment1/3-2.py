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

vis_data = []

dt = dataset.data_table

chauvs = []
mixeds = []
simples = []
localoutliers = []

cs = [0.1, 2, 10]

for i in range(len(cs)):
    c = cs[i]

    data_table = dt.copy()

    chauvs.append(distribution_bod.chauvenet(
        data_table, "acc_phone_x", c=c))
    '''
    mixeds.append(distribution_bod.mixture_model(data_table, "acc_phone_x"))

    simples.append(distance_bod.simple_distance_based(
        data_table, ["acc_phone_x"], "euclidean", c, 1/c))

    localoutliers.append(distance_bod.local_outlier_factor(
        data_table, ["acc_phone_x"], "euclidean", 2*c))

    '''

for c in chauvs:
    detected = list(map(lambda v: v[1], c.values))
    num_detected = len(list(filter(lambda o: o == False, detected)))
    num_not_detected = len(list(filter(lambda o: o != False, detected)))

    print(num_detected)
    print(num_not_detected)

vis.plot_imputed_values(data_table, ["x"] + ["x for c = {}".format(cs[i])
                                             for i in range(len(chauvs))], 'acc_phone_x', chauvs[0], chauvs[1], chauvs[2])
