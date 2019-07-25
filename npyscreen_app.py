import npyscreen
import random
import os

class VaultApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', myStartPipScreen, name='New Pip-Boy 3000')
        self.addForm('PIP', pipMainScreen, name='Pip-Boy 3000')
        self.addForm('INV', inventoryPage, name='INVENTORY')

    def change_form(self, name):
        self.switchForm(name)

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


class inventoryPage(npyscreen.FormWithMenus):
    def afterEditing(self):
        self.parentApp.setNextForm('INV')

    def create(self):
        self.itemOne = baseballBat()
        self.itemTwo = knife()
        self.items = [self.itemOne, self.itemTwo]
        self.inventoryMenu = self.new_menu(name="Inventory")
        self.createNewMenusForItems()

    def selectedMessage(self, nameOfItem):
        npyscreen.notify_confirm("You have selected {0}.".format(nameOfItem), "{0}".format(nameOfItem), editw=1)

    def exit_form(self):
        self.parentApp.switchForm(None)

    def createNewMenusForItems(self):
        item_count = 1
        for item in self.items:
            if (item.count > 0):
                self.item = self.inventoryMenu.addNewSubmenu(item.name, "{0}".format(item_count), self.selectedMessage, [item.name])
                # TODO add refresh page to not show these if item.count > 0
                self.item.addItem("Equip", onSelect=item.equip, shortcut="E")
                self.item.addItem("Repair", onSelect=item.repair, shortcut="R")
                self.item.addItem("Drop", onSelect=item.drop, shortcut="D")
                item_count += 1


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

class knife(weapon):
    def __init__(self):
        self.name = "Knife"
        self.count = 1
        self.condition = 25
        self.equipped = False

#def pipFunc(*args):
#    F = myStartPipScreen(name = "New Pip-Boy")
#    F.edit()
#    return "Created record for " + F.myName.value

if __name__ == '__main__':
    TestApp = VaultApp().run()
