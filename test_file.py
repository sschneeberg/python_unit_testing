import unittest
from file import File

class TestFile(unittest.TestCase):

    def setUp(self):
        print('set up')
        self.file1 = File('testfile1', 'docx')
        self.file2 = File('testfile2', 'pdf')
        self.file3 = File('testfile3', 'py')

    def tearDown(self):
        print('tear down')

    def test_save(self):
        self.file1.save_file('/documents')
        self.assertEqual(self.file1.location, '/documents')
        self.assertEqual(self.file1.size, 1)
        self.file3.save_file('usr/local')
        self.assertEqual(self.file3.location, 'usr/local')
        self.assertEqual(self.file3.size, 1)
        
        with self.assertRaises(ValueError):
            self.file2.save_file('')

        self.assertEqual(self.file2.size, "unsaved")
        
    def test_add(self):
        self.file1.add_to_file()
        self.assertEqual(self.file1.size, 2)
        self.assertEqual(self.file2.size, "unsaved")

if __name__ == '__main__':
    unittest.main()