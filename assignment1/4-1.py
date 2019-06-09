from FrequencyAbstraction import FourierTransformation
from CreateDataset import CreateDataset
from VisualizeDataset import VisualizeDataset

dataset = CreateDataset("./", 1000)
ft = FourierTransformation()
vd = VisualizeDataset()

dataset.add_numerical_dataset(
    "chapter2_result.csv", "timestamps", ["acc_phone_x"])


data = dataset.data_table.to_numpy()
formatted_data = list(map(lambda v: v[0], data))

d = ft.abstract_frequency(dataset.data_table, ["acc_phone_x"], 100, 10)


# def abstract_frequency(self, data_table, cols, window_size, sampling_rate):

#real, imag = ft.find_fft_transformation(formatted_data, 10)

# vd.plot_fourier_amplitudes()

# def plot_fourier_amplitudes(self, freq, ampl_real, ampl_imag):

# print(formatted_data[:2])
# print(real[:3])
