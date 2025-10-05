import unittest

from Doctors import Doctor


class MyTestCase(unittest.TestCase):
    def test_Doctors(self):
        doc = Doctor("sam", "catdiology", "056783456", "1-2")
        self.assertEqual(doc.name, "sam")
        doc.name = "samuel"
        self.assertEqual("samuel", doc.name)  # add assertion here



    def test_Doctors_list(self):
        doc = Doctor("sam", "catdiology", "056783456", "1-2")
        self.assertEqual("sam",doc.DOCTORS[0])




if __name__ == '__main__':
    unittest.main()
