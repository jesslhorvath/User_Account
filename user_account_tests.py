from user_account import user_account as ua
import unittest

class user_account_test(unittest.TestCase):
    def setUp(self):
        self.test_account = ua("Saving", "Peter Pan", 201, 500)

    def tearDown(self):
        del self.test_account

    
    def test_account_attributes(self):
        self.assertEqual(self.test_account.type, "Saving")
        self.assertEqual(self.test_account.owner, "Peter Pan")
        self.assertEqual(self.test_account.number, 201)
        self.assertEqual(self.test_account.balance, 500)

    def test_account_methods(self):
        self.assertEqual(self.test_account.deposit(50), "Deposited $50, New balance:$550")
        self.assertEqual(self.test_account.withdrawal(50), "Withdrew $50, New balance:$500")
        self.assertEqual(self.test_account.display(), f"Account type: Saving\nAccount owner: Peter Pan\nAccount number: 201\nAccount balance: $500.00")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False) 
    