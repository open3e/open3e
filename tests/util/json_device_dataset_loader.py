import json

def load_test_data_file(file_path):
  with open(file_path, "r") as file:
    return json.load(file)

def device_dataset(file_path):
  data = load_test_data_file(file_path)

  datasets = []
  for ecu, datapoint_description in data.items():
    for did_key, did_value in datapoint_description.items():
      datasets.append((ecu, int(did_key), _did_value_as_str(did_value)))
  return datasets

def _did_value_as_str(expected_value):
  if isinstance(expected_value, dict):
    return json.dumps(expected_value)
  # TODO: check how list results are represented as string in open3e, is str([x,y]) enough?
  else:
    return str(expected_value)