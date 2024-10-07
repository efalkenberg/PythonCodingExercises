from collections import defaultdict
import os.path
import unittest


class LogParser:
    """
    A simple log parser that filters log files by
    log level. See `parse()` for details.

    Optimized for zookeeper log files, tests are based on
    https://github.com/logpai/loghub/blob/master/Zookeeper/Zookeeper_2k.log_structured.csv
    """

    def parse(self, files: list, filter_levels: list):
        """
        Parses the given files for the filter levels given and
        writes the matching rows into new files of the following
        format: <input_file>.<level>.filtered.csv.
        Files will only be created if at least one row was found
        matching the given level filter.

        :param files: A list of relative paths of files to be
        parsed. Needs to be of the format:
        `LineId,Date,Time,Level,Node,Component,Id,Content,EventId,EventTemplate`

        :param filter_levels: List of levels (3rd field in the CSV)
        to filter the given files for.
        Levels must be of value `("WARN"|"INFO"|"ERROR")`

        :return: None
        """
        files = files
        filter_levels = filter_levels
        filtered_values = defaultdict(list)

        for file in files:
            with open(file, "r") as log_file:
                for line in log_file:
                    line_parts = line.split(",")
                    if len(line_parts) > 4 and line_parts[4] in filter_levels:
                        filtered_values[line_parts[4]].append(line)

            for level, list_of_rows in filtered_values.items():
                result_file_name = f"{file}.{level}.filtered.csv"
                with open(result_file_name, "w") as filtered_log_file:
                    filtered_log_file.write("".join(list_of_rows))
                    print(f"{len(list_of_rows)} rows written to `{result_file_name}`")


class TestLogParser(unittest.TestCase):
    def test_zookeeper_log_error(self):
        input_file = "files/Zookeeper_2k.log_structured.csv"
        output_file = "files/Zookeeper_2k.log_structured.csv.ERROR.filtered.csv"
        log_parser = LogParser()
        log_parser.parse([input_file], ["ERROR"])
        self.assertTrue(os.path.isfile(output_file))
        with open(output_file, "r") as result_file:
            line_count = len(result_file.readlines())
            self.assertEqual(line_count, 13)

    def test_zookeeper_log_error_and_info(self):
        input_file = "files/Zookeeper_2k.log_structured.csv"
        output_file_error = "files/Zookeeper_2k.log_structured.csv.ERROR.filtered.csv"
        output_file_info = "files/Zookeeper_2k.log_structured.csv.INFO.filtered.csv"
        log_parser = LogParser()
        log_parser.parse([input_file], ["ERROR", "INFO"])

        self.assertTrue(os.path.isfile(output_file_error))
        with open(output_file_error, "r") as result_file:
            line_count = len(result_file.readlines())
            self.assertEqual(line_count, 13)

        self.assertTrue(os.path.isfile(output_file_info))
        with open(output_file_info, "r") as result_file:
            line_count = len(result_file.readlines())
            self.assertEqual(line_count, 669)

        os.remove(output_file_error)
        os.remove(output_file_info)

    def test_zookeeper_log_invalid_level(self):
        input_file = "files/Zookeeper_2k.log_structured.csv"
        output_file = "files/Zookeeper_2k.log_structured.csv.FOO.filtered.csv"
        log_parser = LogParser()
        log_parser.parse([input_file], ["FOO"])
        self.assertFalse(os.path.isfile(output_file))

    def test_zookeeper_log_error_info_separate(self):
        """
        Same as before but with two separate calls
        of `parse()` which should lead to the same result.
        Besides the consistency this also helps to verify
        that the instance does not keep internal state.
        :return:
        """
        input_file = "files/Zookeeper_2k.log_structured.csv"
        output_file_error = "files/Zookeeper_2k.log_structured.csv.ERROR.filtered.csv"
        output_file_info = "files/Zookeeper_2k.log_structured.csv.INFO.filtered.csv"
        log_parser = LogParser()
        log_parser.parse([input_file], ["ERROR"])
        log_parser.parse([input_file], ["INFO"])

        self.assertTrue(os.path.isfile(output_file_error))
        with open(output_file_error, "r") as result_file:
            line_count = len(result_file.readlines())
            self.assertEqual(line_count, 13)

        self.assertTrue(os.path.isfile(output_file_info))
        with open(output_file_info, "r") as result_file:
            line_count = len(result_file.readlines())
            self.assertEqual(line_count, 669)

        os.remove(output_file_error)
        os.remove(output_file_info)
