from easygui import *

# egStore
users = read_or_create_settings("users.txt")

class Settings(EgStore):
  def __init__(self, filename):
    self.firstname = ""
    self.lastname = ""
    self.email = ""
    self.phone = ""
    self.filename = filename
    restore()

# function
def newUser():
  settingsFilename = "user.txt"
  s = Settings(settingsFilename)

  s.firstname = input("Prénom : ")
  s.lastname = input("Nom : ")
  s.email = input("Email : ")
  s.phone = input("Téléphone : ")

def newOrder():



# execution

