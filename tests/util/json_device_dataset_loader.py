import json

def load_test_data_file(file_path):
  with open(file_path, "r") as file:
    return json.load(file)


def read_dataset(file_path):
  data = load_test_data_file(file_path)

  datasets = []
  for ecu, datapoint_description in data.items():
    for did_key, did_value in datapoint_description.items():
      datasets.append((ecu, int(did_key), __did_value_as_str(did_value)))
  return datasets


def read_dataset_dict(file_path):
  data_set_list = read_dataset(file_path)

  result = {}
  for ecu, did_key, did_value in data_set_list:
    if ecu not in result:
      result[ecu] = {}
    result[ecu][did_key] = did_value
  return result


def write_dataset(file_path):
  data = load_test_data_file(file_path)

  datasets = []
  for ecu, datapoint_description in data.items():
    for did_key, did_values in datapoint_description.items():
      datasets.append((ecu, int(did_key), __did_value_as_str(did_values["initial"]), __did_value_as_str(did_values["to_write"])))
  return datasets


def write_dataset_dict(file_path):
  data_set_list = write_dataset(file_path)

  result = {}
  for ecu, did_key, did_value_initial, did_value_to_write in data_set_list:
    if ecu not in result:
      result[ecu] = {}

    if did_key not in result[ecu]:
      result[ecu][did_key] = {}

    result[ecu][did_key]["initial"] = did_value_initial
    result[ecu][did_key]["to_write"] = did_value_to_write
  return result


def __did_value_as_str(expected_value):
  if isinstance(expected_value, dict):
    return json.dumps(expected_value)
  # TODO: check how list results are represented as string in open3e, is str([x,y]) enough?
  else:
    return str(expected_value)