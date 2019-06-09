from FrequencyAbstraction import FourierTransformation
from CreateDataset import CreateDataset
from VisualizeDataset import VisualizeDataset

dataset = CreateDataset("./", 1000)
ft = FourierTransformation()
vd = VisualizeDataset()

dataset.add_numerical_dataset(
    "chapter2_result.csv", "timestamps", ["acc_phone_x"])

frequencies = ft.abstract_frequency(
    data_table=dataset.data_table, cols=["acc_phone_x"], window_size=100, sampling_rate=10)

frequencies_numpy = frequencies.to_numpy()
formatted_frequencies = list(map(lambda v: v[0], frequencies_numpy))

real, imag = ft.find_fft_transformation(
    data=formatted_frequencies, sampling_rate=10)

vd.plot_fourier_amplitudes(formatted_frequencies, real, imag)

# def abstract_frequency(self, data_table, cols, window_size, sampling_rate):

#real, imag = ft.find_fft_transformation(formatted_data, 10)

# vd.plot_fourier_amplitudes()

# def plot_fourier_amplitudes(self, freq, ampl_real, ampl_imag):

# print(formatted_data[:2])
# print(real[:3])
