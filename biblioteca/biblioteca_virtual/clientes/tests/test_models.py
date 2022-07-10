import unittest

class TestCliente(unittest.TestCase):
    def test_nome(self):
       nome= 'Raquel'
       self.assertEquals('Mariana', nome)
        
if __name__ =='__name__':
    unittest.main()