import unittest
import pyperclip
from credential import Credential

class TestCredential(unittest.TestCase):
  '''
  Test class that defines test cases for the credential class behaviours.

  Args:
    unittest.TestCase: TestCase class that helps in creating credential test cases
  '''
  def setUp(self):
    '''
    Set up method to run before each test cases in credential
    '''
    self.new_credential = Credential("NgetichNick","NICK1234","0725470732") #creating credential object

  def tearDown(self):
    '''
    tearDown method that does clean up after each test case has run.
    '''
    Credential.credential_list = []

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_credential.credential_name,"NgetichNick")
    self.assertEqual(self.new_credential.password,"NICK1234")
    self.assertEqual(self.new_credential.number,"0725470732")
  def test_save_credential(self):
    '''
    test_save_credential test case to test if the credential object is saved into
    the credential list
    '''
    self.new_credential.save_credential() #saving the credential
    self.assertEqual(len(Credential.credential_list),1)

  def test_save_multiple_credential(self):
    '''
    test_save_multiple_credential to check if we can save multiple contact
    objects to our contact list
    '''
    self.new_credential.save_credential()
    test_credential = Credential("NickKorgoren","Better00","0714042437") #new credential
    test_credential.save_credential()
    self.assertEqual(len(Credential.credential_list),2)

  def test_delete_credential(self):
    '''
    test_delete_credential to test if we can remove a credential from our credential list
    '''
    self.new_credential.save_credential()
    test_credential = Credential("NickKorgoren","Better00","0714042437") #new credential
    test_credential.save_credential()

    self.new_credential.delete_credential() #Deleting a credential object
    self.assertEqual(len(Credential.credential_list),1)

  def test_find_credential_by_number(self):
    '''
    test to check if we can find a credential by phone number and display information
    '''
