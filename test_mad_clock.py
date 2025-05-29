import unittest
from unittest.mock import patch, mock_open, MagicMock
from main import MadClock
import builtins
import json

class TestMadClock(unittest.TestCase):
    def setUp(self):
        self.clock = MadClock()

    @patch("main.os.path.exists", return_value=False)
    def test_default_time_format_when_no_settings_file(self, mock_exists):
        clock = MadClock()
        self.assertEqual(clock.time_format, "24h")

    @patch("main.os.path.exists", return_value=True)
    @patch("main.open", new_callable=mock_open, read_data='{"time_format": "12h"}')
    def test_load_time_format_from_settings_file(self, mock_file, mock_exists):
        clock = MadClock()
        self.assertEqual(clock.time_format, "12h")

    @patch("main.open", new_callable=mock_open)
    def test_save_settings_writes_correct_format(self, mock_file):
        self.clock.time_format = "12h"
        self.clock.save_settings()
        mock_file().write.assert_called_once_with(json.dumps({"time_format": "12h"}))

    def test_toggle_format_changes_value(self):
        original_format = self.clock.time_format
        self.clock.toggle_format()
        self.assertNotEqual(self.clock.time_format, original_format)

    def test_get_time_format_output_24h(self):
        self.clock.time_format = "24h"
        time_str = self.clock.get_time()
        self.assertRegex(time_str, r"\d{2}:\d{2}")

    def test_get_time_format_output_12h(self):
        self.clock.time_format = "12h"
        time_str = self.clock.get_time()
        self.assertRegex(time_str, r"\d{2}:\d{2} (AM|PM)")

    @patch("builtins.print")
    def test_show_reverse_prints_something(self, mock_print):
        self.clock.show_reverse()
        self.assertTrue(mock_print.called)

    @patch("builtins.print")
    def test_show_binary_prints_binary_values(self, mock_print):
        self.clock.show_binary()
        self.assertTrue(mock_print.called)

    @patch("builtins.print")
    def test_show_hex_prints_hex_values(self, mock_print):
        self.clock.show_hex()
        self.assertTrue(mock_print.called)

    @patch("builtins.print")
    def test_show_morse_prints_morse_code(self, mock_print):
        self.clock.show_morse()
        self.assertTrue(mock_print.called)

    @patch("main.input", side_effect=["format", "exit"])
    @patch("builtins.print")
    def test_run_with_toggle_and_exit(self, mock_print, mock_input):
        with patch.object(self.clock, 'toggle_format') as mock_toggle:
            self.clock.run()
            mock_toggle.assert_called_once()
            mock_print.assert_any_call('\x1b[36m' + "Goodbye!")

    @patch("main.input", side_effect=["invalid", "exit"])
    @patch("builtins.print")
    def test_run_with_invalid_input(self, mock_print, mock_input):
        self.clock.run()
        mock_print.assert_any_call('\x1b[31m' + "Invalid mode. Please choose from: morse, binary, reverse.")
