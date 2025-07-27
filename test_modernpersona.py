# test_modernpersona.py
"""
Tests for ModernPersona module.
"""

import unittest
from modernpersona import ModernPersona

class TestModernPersona(unittest.TestCase):
    """Test cases for ModernPersona class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ModernPersona()
        self.assertIsInstance(instance, ModernPersona)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ModernPersona()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
