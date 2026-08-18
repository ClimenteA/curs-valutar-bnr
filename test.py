import datetime
import unittest
from unittest.mock import patch

from src.cursvalutarbnr import Currency, ron_exchange_rate


class RonExchangeRateTest(unittest.TestCase):
    def test_convert_one_eur(self):
        rates = {"2024-01-03": {"EUR": 4.9771}}
        with patch("src.cursvalutarbnr.get_bnr_rates", return_value=rates):
            result = ron_exchange_rate(1, Currency.EUR, "2024-01-03")
        self.assertEqual(result, 4.9771)

    def test_convert_multiplies_amount(self):
        rates = {"2024-01-03": {"EUR": 4.9771}}
        with patch("src.cursvalutarbnr.get_bnr_rates", return_value=rates):
            result = ron_exchange_rate(2, Currency.EUR, "2024-01-03")
        self.assertEqual(result, 9.9542)

    def test_accepts_currency_as_string(self):
        rates = {"2024-01-03": {"EUR": 4.9771}}
        with patch("src.cursvalutarbnr.get_bnr_rates", return_value=rates):
            result = ron_exchange_rate(1, "EUR", "2024-01-03")
        self.assertEqual(result, 4.9771)

    def test_unsupported_currency_raises_value_error(self):
        with self.assertRaises(ValueError):
            ron_exchange_rate(1, "BTC", "2024-01-03")

    def test_accepts_date_object(self):
        rates = {"2024-01-03": {"EUR": 4.9771}}
        with patch("src.cursvalutarbnr.get_bnr_rates", return_value=rates):
            result = ron_exchange_rate(1, Currency.EUR, datetime.date(2024, 1, 3))
        self.assertEqual(result, 4.9771)

    def test_default_date_uses_available_rates(self):
        rates = {"2024-01-03": {"EUR": 4.9771}}
        with patch("src.cursvalutarbnr.get_bnr_rates", return_value=rates):
            result = ron_exchange_rate(1, Currency.EUR)
        self.assertEqual(result, 4.9771)

    def test_rounds_to_four_decimals(self):
        rates = {"2024-01-03": {"EUR": 4.97715}}
        with patch("src.cursvalutarbnr.get_bnr_rates", return_value=rates):
            result = ron_exchange_rate(1, Currency.EUR, "2024-01-03")
        self.assertEqual(result, 4.9772)

    def test_closest_available_date(self):
        rates = {
            "2024-01-03": {"EUR": 4.97},
            "2024-01-08": {"EUR": 4.99},
        }
        with patch("src.cursvalutarbnr.get_bnr_rates", return_value=rates):
            result = ron_exchange_rate(1, Currency.EUR, "2024-01-05")
        self.assertEqual(result, 4.97)

    def test_jan_1_uses_previous_year(self):
        rates = {
            "2023-12-29": {"EUR": 4.96},
            "2024-01-03": {"EUR": 4.97},
        }
        with patch("src.cursvalutarbnr.get_bnr_rates", return_value=rates):
            result = ron_exchange_rate(1, Currency.EUR, "2024-01-01")
        self.assertEqual(result, 4.96)


if __name__ == "__main__":
    unittest.main()
