from CreateDataset import CreateDataset
import numpy as np


dataset = CreateDataset("./", 1000)
dataset2 = CreateDataset("./", 1000)

# dataset.add_numerical_dataset(
#    "5_LSM6DSL_Gyroscope_Sensor.csv", "timestamp", ["y"])

dataset.add_numerical_dataset(
    "chapter2_result.csv", "timestamps", ["acc_phone_x"])

dataset2.add_numerical_dataset(
    "5_LSM6DSL_Acceleration_Sensor.csv", "timestamp", ["x"])

their = [v[0] for v in dataset.data_table.values]
mine = [v[0] for v in dataset2.data_table.values]

their = np.array(their)
mine = np.array(mine)

their_mean = their.mean()
their_std = their.std()

mine_mean = mine.mean()
mine_std = mine.std()

print("Mean of crowdsignals acceleration x axis: {} with std: {}".format(
    their_mean, their_std))
print("Mean of gathered  acceleration x axis: {} with std: {}".format(
    mine_mean, mine_std))
