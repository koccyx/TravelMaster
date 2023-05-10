import unittest
from userPanel import *

class UnitTest(unittest.TestCase):
	def test_Int(self):
		self.assertRaises(ValueError, pdfTicketID, -2)

if __name__ == '__main__':
	unittest.main()