import unittest
from Patients import Patient

class MyTestCase(unittest.TestCase):
    def test_Doctors(self):
        pat = Patient("Emma",44, "089876567", "Headache")
        self.assertEqual(pat.name,"Emma")
        pat.name = "Emmanuel"
        self.assertEqual(pat.name,"Emmanuel")

    def test_list_of_patients(self):
        pat = Patient("Emma", "089876567", "Headache")
        pat2 = Patient("Emm", "089867", "Headache and stomach")
        self.assertEqual(pat.Pateints, "[Emma, Emm]")


if __name__ == '__main__':
    unittest.main()
