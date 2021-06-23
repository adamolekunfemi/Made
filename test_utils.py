import pytest
import utils

class TestUtils(object):
    def test_file_without_json_extension(self):
        actual = utils.transform_events_data("events_data-2020-07-01.csv")
        assert actual == "events_data-2020-07-01.csv", "Expected: events_data-2020-07-01.json, Actual: {0}".format(actual)

    def test_file_less_than_three_hyphen(self):
        actual = utils.transform_events_data("events_data_2020-07-01.json")
        assert actual == "events_data-2020-07-01.json", "Expected: events_data-2020-07-01.json, Actual: {0}".format(actual)

    def test_file_without_underscore(self):
        actual = utils.transform_events_data("events_data_2020-07-01.json")
        assert actual == "events-data-2020-07-01.json", "Expected: events_data-2020-07-01.json, Actual: {0}".format(actual)

    def test_file_with_dot(self):
        actual = utils.transform_events_data("events_data_2020-07-01.json")
        assert actual == "events_data_2020-07-01json", "Expected: events_data-2020-07-01.json, Actual: {0}".format(actual)



if __name__ == '__main__':
   pytest.main()

