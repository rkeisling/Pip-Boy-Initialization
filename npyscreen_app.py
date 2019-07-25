import npyscreen
import random
from consolemenu import *
from consolemenu.items import *

class VaultApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', myStartPipScreen, name='New Pip-Boy 3000')
        self.addForm('PIP', pipMainScreen, name='Pip-Boy 3000')
        self.addForm('INV', inventoryPage, name='INVENTORY')

    def change_form(self, name):
        self.switchForm(name)
        self.resetHistory

class myStartPipScreen(npyscreen.ActionForm):
    def afterEditing(self):
        self.parentApp.setNextForm('PIP')

    def create(self):
        self.myName = self.add(npyscreen.TitleText,
                               name="Your name here:",
                               begin_entry_at=16,
                               use_two_lines=False)
        self.myVault = self.add(npyscreen.TitleSelectOne,
                                max_height=5,
                                name='Vault',
                                values = ['101', '111', '108', '77', '81'],
                                scroll_exit = True)
    def on_ok(self):
        self.userId = random.randrange(1,100000)
        self.userGreeting = "User " + str(self.userId)
        npyscreen.notify_wait("Welcome to the future, {0}.".format(self.userGreeting), title="WELCOME")
        npyscreen.notify_confirm("Vault-Tec and ROBCO Industries are not responsible for bodily harm resulting from use of the Pip-Boy 3000. Please consult your handbook for all guidelines and warnings.", editw=1, title="WARNING")
        exiting = npyscreen.notify_yes_no("Do you agree to the terms and conditions set forth by the handbook at this time?", title="TERMS & CONDITIONS", editw=1)
        if (exiting):
            npyscreen.notify_wait("Thank you. Proceeding...")
        else:
            npyscreen.notify_wait("The Pip-Boy 3000 will now power off.")

    def on_cancel(self):
        npyscreen.notify_wait("The Pip-Boy 3000 will now power off.")

class pipMainScreen(npyscreen.ActionFormV2WithMenus):

    def create(self):
    #    navigationOptions = ['STATUS', 'INVENTORY', 'DATA', 'MAP', 'RADIO']
    #    self.option = self.add(npyscreen.TitleSelectOne,
    #                           name='Options',
    #                           values = navigationOptions,
    #                           scroll_exit = True)
        self.invButton = self.add(npyscreen.Button, name='INVENTORY', value_changed_callback=self.invButtonPress)

    def invButtonPress(self, widget):
        npyscreen.notify_wait("ACCESSING INVENTORY...")
        self.parentApp.change_form('INV')

    def on_ok(self):
        selection = self.option.get_selected_objects()[0]
        if (selection == 'INVENTORY'):
            npyscreen.notify_wait("ACCESSING INVENTORY...")

            self.parentApp.change_form('INV')

        else:
            npyscreen.notify_wait("I don't know how it got to this.")


class inventoryPage(npyscreen.ActionFormV2WithMenus):
    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
        #itemOne = baseballBat()
        #self.inventoryMenu = self.new_menu(name="Inventory", shortcut="i")

        #self.itemOneMenu = self.inventoryMenu.addNewSubmenu(itemOne.name, "1", self.press_1)
        #self.itemOneMenu.addItem("Equip", onSelect=itemOne.equip, shortcut="E")
        #self.itemOneMenu.addItem("Repair", onSelect=itemOne.repair, shortcut="R")
        #self.itemOneMenu.addItem("Drop", onSelect=itemOne.drop, shortcut="D")

        #self.inventoryMenu.addItem("Knife", self.press_2, "2")
        #self.inventoryMenu.addItem("Exit Inventory", self.exit_form, "^X")
        showOtherMenu("Inventory", "This is inv")


    def press_1(self):
        npyscreen.notify_confirm("You have selected Baseball Bat.", "Baseball Bat", editw=1)

    def press_2(self):
        npyscreen.notify_confirm("You have selected Knife.", "Knife", editw=1)

    def exit_form(self):
        self.parentApp.switchForm(None)

def showOtherMenu(title, subtitle):
    menu = ConsoleMenu(title, subtitle)

    menu_item = MenuItem("Menu Item")

    function_item = FunctionItem("Call a python function.", input, ["Enter an input"])

    command_item = CommandItem("Run a console command!", "touch hello.txt")

    selection_menu = SelectionMenu(["item1", "item2", "item3"])

    submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

    menu.append_item(menu_item)
    menu.append_item(function_item)
    menu.append_item(command_item)
    menu.append_item(submenu_item)

    menu.show()

class weapon:
    def drop(self):
        if (self.count > 0):
            self.count -= 1
            npyscreen.notify_wait("You have dropped one of {0}.".format(self.name))
        else:
            npyscreen.notify_wait("Failed to drop {0}. Item count too low ({1})".format(self.name, self.count))

    def equip(self):
        if (self.equipped == False):
            self.equipped = True
            npyscreen.notify_wait("You have equipped {0}. Condition is {1}.".format(self.name, self.condition))
        else:
            self.equipped = False
            npyscreen.notify_wait("You have unequipped {0}.".format(self.name))

    def repair(self):
        if (self.condition < 100):
            self.condition += 25
            npyscreen.notify_wait("You have repaired {0}. Condition is now {1}.".format(self.name, self.condition))
        else:
            npyscreen.notify_wait("{0} already at max condition.".format(self.name))

    def __init__(self):
        self.name = ""
        self.count = 0
        self.condition = 0
        self.equipped = False


class baseballBat(weapon):
    def __init__(self):
        self.name = "Baseball Bat"
        self.count = 1
        self.condition = 50
        self.equipped = False



#def pipFunc(*args):
#    F = myStartPipScreen(name = "New Pip-Boy")
#    F.edit()
#    return "Created record for " + F.myName.value

if __name__ == '__main__':
    TestApp = VaultApp().run()
