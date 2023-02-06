from rpg_lib import Location, Player, Game, Item, EnemyQuestion, QuestionHandler, Question, Logic, NPC, Quest, QuestItem
from typing import Type

yourBedroom = Location(id=0, name="your bedroom", description="This is your cozy little bedroom.", items=[], entities=[])
livingRoom = Location(id=1, name="the living room", description="You enter the living room you've known all your life, it seems to be in disarray.", items=[], entities=[])
kitchen = Location(id=2, name="the kitchen", description="You enter the kitchen opposite of the living room, it's a mess.", items=[], entities=[])
attic = Location(id=3, name="the attic", description="You feel a strange presence from the ladder to the attic. You get the feeling the source of all this strangeness is coming from up here.", items=[], entities=[])
yourBedroom.change_west(livingRoom)
yourBedroom.change_east(kitchen)
livingRoom.change_south(attic)
livingRoom.change_east(yourBedroom)
player = Player(1, "test", 3, yourBedroom)

class GoLogic(Logic):
    def __init__(self) -> None:
        super().__init__()
    
    def execute(self, player: Type[Player], arguments: list[str]) -> None:
        player.change_location(direction=arguments[0])

class UseLogic(Logic):
    def __init__(self) -> None:
        super().__init__()
    
    def execute(self, player: Type[Player], arguments: list[str]) -> None:
        itemIndex:int = player.get_item_name_index(itemName=" ".join(arguments))
        if itemIndex != None:
            player.inventory[itemIndex].use(player)
            return None
        print("Item does not exist!\n")

class PickUpLogic(Logic):
    def __init__(self) -> None:
        super().__init__()
    
    def execute(self, player: Type[Player], arguments: list[str]) -> None:
        itemsOnGround:list[Type[Item]] = player.currentLocation.items
        itemName:str = " ".join(arguments)
        for i in itemsOnGround:
            if i.name == itemName:
                player.add_item_to_inventory(item=i)
                player.currentLocation.items.remove(i)
                print("{} has been added to your inventory.\n".format(i.name))
                return None
        else:
            print("No such item on the ground.\n")
            return None

class CheckInventoryLogic(Logic):
    def __init__(self) -> None:
        super().__init__()
    
    def execute(self, player: Type[Player], arguments: list[str]) -> None:
        print("\nThe Items on your inventory are...")
        print(", ".join(i.name for i in player.inventory))
        print()

class TalkLogic(Logic):
    def __init__(self) -> None:
        super().__init__()
    
    def execute(self, player: Type[Player], arguments: list[str]) -> None:
        npcName = " ".join(arguments)
        for i in player.currentLocation.entities:
            if i.name.lower() == npcName:
                print()
                i.behavior(player)

class TestItem(Item):
    def __init__(self, id: int, name: str) -> None:
        super().__init__(id, name)
    
    def use(self, player: Type[Player]) -> None:
        print("hello, world!")

#livingRoom.add_item_on_ground(TestItem(1, "test item"))


#testNPC = NPC(1, "John Doe", "Villager")
#testNPC.add_dialogue("Hello there!")
#testNPC.set_thanks_dialogue("Thank you so much! Here, take this test reward item.")
#livingRoom.add_entity_on_location(testNPC)
#testReward = Item(2, "test reward item")


#testQuestItem = QuestItem(1, "test quest item")
#kitchen.add_item_on_ground(testQuestItem)


#testQuest = Quest(questItem=testQuestItem, rewardItem=testReward)
#testNPC.set_quest(testQuest)

#testQuest.add_quest_dialogue("I need an item called test quest item. For it, I will give you test reward item.")

#kitchen.add_item_on_ground(testQuestItem)

    questionHandler = QuestionHandler()
    ghostQuestion = Question("What's 1 + 1?", "2")
    zombieQuestion = Question("What's 42 in binary?", "101010")
    questionHandler.add_question(ghostQuestion)
    questionHandler.add_question(zombieQuestion)

    ghost = EnemyQuestion(1, "What seems to be a person flailing around under a blanket", 1, questionHandler)
    zombie = EnemyQuestion(2, "Somebody with terrible cuts all over their body", 1, questionHandler)
    livingRoom.add_entity_on_location(ghost)
    kitchen.add_entity_on_location(zombie)

    if ghost.check_alive() is False:
        ghost = None
        #livingRoom.remove_entity_on_location(ghost)
        #livingRoom.remove_enemy_on_location(ghost)
    if zombie.check_alive() is False:
        zombie = None
        #kitchen.remove_entity_on_location(zombie)
        #kitchen.remove_enemy_on_location(zombie)

game = Game(player=player)

# print(testQuestItem.id)

game.add_command("go", GoLogic())
game.add_command("use", UseLogic())
game.add_command("take", PickUpLogic())
game.add_command("inventory", CheckInventoryLogic())
game.add_command("talk", TalkLogic())

if __name__ == '__main__':
    playerName = str(input("What is your name, young one? "))
    player.set_name(playerName)
    print("I see, nice to meet you {}!".format(player.get_name()))
    game.run()

game.run()
