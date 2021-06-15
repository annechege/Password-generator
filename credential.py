import pyperclip
class Credential:
  """
  a class that creates new credentials for credentials
  """
  credential_list = []

  def __init__(self, credential_name, password,number):
    self.credential_name = credential_name
    self.password = password
    self.number = number
    def save_credential(self):
    '''
    save_credential method saves credential object into the credential_list
    '''

    Credential.credential_list.append(self)

  def delete_credential(self):
    '''
    delete_credential method deletes a saved credential from the credential_list
    '''

    Credential.credential_list.remove(self)