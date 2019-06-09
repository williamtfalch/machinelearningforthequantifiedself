import ast
from CreateDataset import CreateDataset


dataset = CreateDataset("./", 1000)

dataset.add_numerical_dataset(
    "5_LSM6DSL_Gyroscope_Sensor.csv", "timestamp", ["y"])

print(dataset.data_table)
