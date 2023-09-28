import unittest

from fixerio.fixerio_client import FixerioClient


class FixerioInitTestCase(unittest.TestCase):
    def test_raises_if_access_key_is_not_passed(self):
        with self.assertRaises(TypeError):
            FixerioClient()

    def test_sets_access_key(self):
        access_key = "test-access-key"

        client = FixerioClient(access_key)

        self.assertEqual(client.access_key, access_key)

    def test_sets_none_symbols_attribute_if_it_is_not_passed(self):
        client = FixerioClient("test-access-key")

        self.assertIsNone(client.symbols)

    def test_sets_symbols_attribute(self):
        symbols = ["USD", "GBP"]

        client = FixerioClient("test-access-key", symbols=symbols)

        self.assertEqual(client.symbols, symbols)

    def test_sets_none_base_attribute_if_it_is_not_passed(self):
        client = FixerioClient("test-access-key")

        self.assertIsNone(client.base)

    def test_sets_base_attribute(self):
        base = "USD"

        client = FixerioClient("test-access-key", base=base)

        self.assertEqual(client.base, base)

    def test_sets_base_url_attribute(self):
        base_url = "http://test.url"

        client = FixerioClient("test-access-key")
        client.base_url = base_url

        self.assertEqual(client.base_url, base_url)

    def test_access_key_in_payload(self):
        access_key = "test-access-key"
        expected_payload = {
            "access_key": access_key
        }

        client = FixerioClient("test-access-key")
        payload = client._create_payload()

        self.assertEqual(payload, expected_payload)

    def test_does_not_set_none_payloads(self):
        access_key = "test-access-key"
        payload_param = None
        expected_payload = {
            "access_key": access_key
        }

        client = FixerioClient("test-access-key")
        payload = client._create_payload(payload_param=payload_param)

        self.assertEqual(payload, expected_payload)

    def test_sets_non_none_payloads(self):
        access_key = "test-access-key"
        payload_param = "test-payload"
        expected_payload = {
            "access_key": access_key,
            "payload_param": payload_param
        }

        client = FixerioClient("test-access-key")
        payload = client._create_payload(payload_param=payload_param)

        self.assertEqual(payload, expected_payload)

    def test_list_payloads(self):
        access_key = "test-access-key"
        payload_param = ["a", "b", "c"]
        expected_payload = {
            "access_key": access_key,
            "payload_param": "a,b,c"
        }

        client = FixerioClient("test-access-key")
        payload = client._create_payload(payload_param=payload_param)

        self.assertEqual(payload, expected_payload)

    def test_single_item_list_payloads(self):
        access_key = "test-access-key"
        payload_param = ["a"]
        expected_payload = {
            "access_key": access_key,
            "payload_param": "a"
        }

        client = FixerioClient("test-access-key")
        payload = client._create_payload(payload_param=payload_param)

        self.assertEqual(payload, expected_payload)

    def test_sets_special_payload_mappings(self):
        access_key = "test-access-key"
        from_ccy = "ABC"
        to_ccy = "DEF"
        expected_payload = {
            "access_key": access_key,
            "from": from_ccy,
            "to": to_ccy
        }

        client = FixerioClient("test-access-key")
        payload = client._create_payload(from_ccy=from_ccy, to_ccy=to_ccy)

        self.assertEqual(payload, expected_payload)
