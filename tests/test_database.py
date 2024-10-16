import copy
import unittest
import helpers
import database as db


class TestDabase(unittest.TestCase):
    def setUp(self):
        db.Clients.clientsList = [
            db.Client("37K", "Kasandra", "Salvador"),
            db.Client("23L", "Maria", "Calatayud"),
            db.Client("94S", "Marcos", "Herrero"),
        ]

    def test_search_client(self):
        existing_customer = db.Clients.search("37K")
        nonexisting_customer = db.Clients.search("11A")

        self.assertIsNotNone(existing_customer)
        self.assertIsNone(nonexisting_customer)

    def test_add_client(self):
        new_client = db.Clients.add("49L", "Test", "Test")

        self.assertEqual(len(db.Clients.clientsList), 4)
        self.assertEqual(new_client.dni, "49L")
        self.assertEqual(new_client.name, "Test")
        self.assertEqual(new_client.surname, "Test")

    def test_modify_client(self):
        client_to_modify = copy.copy(db.Clients.search("37K"))
        modified_client = db.Clients.modify("37K", "Manola", "Vasos")

        self.assertEqual(client_to_modify.name, "Kasandra")
        self.assertEqual(modified_client.name, "Manola")

    def test_delete_client(self):
        deleted_client = db.Clients.delete("37K")
        searched_client = db.Clients.search("37K")

        self.assertEqual(deleted_client.dni, "37K")
        self.assertIsNone(searched_client)

    def test_dni_validate(self):
        self.assertTrue(helpers.dni_validate("00X"))
        self.assertFalse(helpers.dni_validate("123214A"))
        self.assertFalse(helpers.dni_validate("F45"))

    def test_ultimate_dni_validate(self):
        self.assertTrue(helpers.ultimate_dni_validate("56F", db.Clients.clientsList))
        self.assertFalse(helpers.ultimate_dni_validate("37K", db.Clients.clientsList))
        self.assertFalse(helpers.ultimate_dni_validate("423523F", db.Clients.clientsList))

