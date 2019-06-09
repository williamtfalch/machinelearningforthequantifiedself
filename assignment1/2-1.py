import ast
from CreateDataset import CreateDataset
from VisualizeDataset import VisualizeDataset
import datetime


def sensorlog2activities(path):
    num_captures = 0
    activities = {}
    logs = {}

    line_counter = 0
    last_activity_id = None  # first id recorded in activitylog.txt
    max_num_lines_per_activity = 10000

    # approved sensors
    approved_sensors = ["LSM6DSL Acceleration Sensor",
                        "LSM6DSL Gyroscope Sensor"]

    # read original file and convert activities to sets of max 10000 lines to save computing power
    with open(path) as f:
        f.readline()

        # add dict of recorded activities
        while True:
            line = f.readline().split("|")

            if line[0] == "statusId":
                break

            else:
                num_captures += 1
                activities[line[0]] = line[1]
                logs[line[0]] = []

        # iterate over sensor readings for activities
        for reading in f:
            values = reading.split("|")

            if values[1] not in approved_sensors:
                continue

            if values[0] == last_activity_id:
                if line_counter >= max_num_lines_per_activity:
                    continue

            else:
                last_activity_id = values[0]
                line_counter = 0

            formatted_values = values[1:2] + \
                ast.literal_eval(values[2]) + values[3:]

            logs[values[0]].append(formatted_values)
            line_counter += 1

        f.close()

    return activities, logs


def average_logs(logs, granularity):
    averaged_logs = {}

    for activity in logs:
        sensors = {}
        timestamps = {}
        averages = {}

        for reading in logs[activity]:
            # print(reading)
            sensor, x, y, z, timestamp = reading
            x = float(x)
            y = float(y)
            z = float(z)
            timestamp = int(timestamp.replace('\n', ''))

            if sensor not in sensors:
                sensors[sensor] = []
                # averages[sensor] = []

                # min, max
                timestamps[sensor] = [1000000000000000, 0]

            sensors[sensor].append((x, y, z, timestamp))

            if timestamp < timestamps[sensor][0]:
                timestamps[sensor][0] = timestamp

            elif timestamp > timestamps[sensor][1]:
                timestamps[sensor][1] = timestamp

        for sensor in sensors:
            averages[sensor] = [[] for _ in range(
                (timestamps[sensor][1] - timestamps[sensor][0])//granularity + 1)]

            for reading in sensors[sensor]:
                averages[sensor][(reading[3] - timestamps[sensor]
                                  [0])//granularity].append(reading[:3])

            for i in range(len(averages[sensor])):
                bracket = averages[sensor][i]
                len_bracket = len(bracket)

                if len_bracket == 0:
                    len_bracket = 1

                x_avg = sum([b[0] for b in bracket])/len_bracket
                y_avg = sum([b[1] for b in bracket])/len_bracket
                z_avg = sum([b[2] for b in bracket])/len_bracket

                epochs = (timestamps[sensor][0] + granularity*i)/1000

                ts = datetime.datetime.fromtimestamp(
                    epochs).strftime('%Y-%m-%d %H:%M:%S')

                averages[sensor][i] = [ts,
                                       str(x_avg), str(y_avg), str(z_avg)]

        averaged_logs[activity] = averages

    return averaged_logs


def averaged_logs2csvs(averaged_logs, activities):
    for activity in averaged_logs:
        for sensor in averaged_logs[activity]:
            readings = averaged_logs[activity][sensor]
            formatted_sensor = sensor.replace(" ", "_")

            with open("./{}_{}.csv".format(activity, formatted_sensor), "w") as f:
                f.write("timestamp,x,y,z\n")

                for reading in readings:
                    f.write(','.join(reading) + "\n")

                f.close()


vd = VisualizeDataset()

activities, logs = sensorlog2activities('./activitylog.txt')
averaged_logs = average_logs(logs, 250)
averaged_logs2csvs(averaged_logs, activities)


dataset = CreateDataset("./", 1000)

dataset.add_numerical_dataset(
    "5_LSM6DSL_Acceleration_Sensor.csv", "timestamp", ["y"])

print(dataset.data_table)

vd.plot_dataset(dataset.data_table, ['y'], "exact")
