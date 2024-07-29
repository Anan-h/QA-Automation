import unittest
from unittest.mock import mock_open, patch
from error_handling_assignment.src.utils.config_provider import ConfigProvider
from error_handling_assignment.src.file_processor import FileProcessor


class TestFileProcessor(unittest.TestCase):
    config = ConfigProvider().load_from_file('config.json')

    def setUp(self):
        self.processor = FileProcessor()

    @patch('builtins.open', new_callable=mock_open)
    def test_write_in_file(self, mock_file):
        self.processor.write_in_file(self.config['file_path'], self.config['content'])

        # tests that open was called with the correct file path and mode
        mock_file.assert_called_with(self.config['file_path'], self.config['write_mode'])

        # tests that the file has the content
        mock_file().write.assert_called_once_with(self.config['content'])

    @patch('builtins.open', new_callable=mock_open, read_data='Hello, World!')
    def test_read_from_file(self, mock_file):
        content = f"File Content: Hello, World!"

        result = self.processor.read_from_file(self.config['file_path'])

        # tests that open was called with the correct file path and mode
        mock_file.assert_called_with(self.config['file_path'], self.config['read_mode'])

        # tests that the result is as expected
        self.assertEqual(result, content)
