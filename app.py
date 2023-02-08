from rpg_lib import Location, Player, Game, Item, EnemyQuestion, QuestionHandler, Question, Logic, NPC, Quest, QuestItem
from typing import Type

yourBedroom = Location(id=0, name="YOUR BEDROOM", description="This is your cozy little bedroom.", items=[], entities=[])
livingRoom = Location(id=1, name="THE LIVING ROOM", description="You enter the living room you've known all your life, it seems to be in disarray.", items=[], entities=[])
kitchen = Location(id=2, name="THE KITCHEN", description="You enter the kitchen opposite of the living room, it's a mess.", items=[], entities=[])
attic = Location(id=3, name="THE ATTIC", description="You've eliminated the Lesser Demon, the source of all this. \nCheck the window to see the state of the world.", items=[], entities=[])
window = Location (id=4,name="THE ATTIC WINDOW", description="A blinding light fills your vision. \nIt was all a dream. \nThe end.", items=[], entities=[])
hiddenRoom = Location(id=5, name="a hidden room in the kitchen", description="It seems there was a hidden room in the kitchen.", items=[], entities=[])
secretTunnel = Location(id=6, name="a secret tunnel", description="The hidden room lead you to a secret tunnel?", items=[], entities=[])
treasureRoom = Location(id=7, name="a treasure room at the end of the tunnel.", description="What seems to be a room full of treasure awaits you. \nWhat's this place doing in your house?", items=[], entities=[])

yourBedroom.change_west(livingRoom)
yourBedroom.change_east(kitchen)
livingRoom.change_south(attic)
livingRoom.change_east(yourBedroom)
kitchen.change_west(yourBedroom)
kitchen.change_south(hiddenRoom)
hiddenRoom.change_north(kitchen)
hiddenRoom.change_south(secretTunnel)
secretTunnel.change_north(hiddenRoom)
secretTunnel.change_south(treasureRoom)
treasureRoom.change_north(secretTunnel)
attic.change_south(window)
attic.change_north(livingRoom)
player = Player(1, "test", 3, yourBedroom)

class GoLogic(Logic):
    def __init__(self) -> None:
        super().__init__()
    
    def execute(self, player: Type[Player], arguments: list[str]) -> None:
        player.change_location(direction=arguments[0])
        player.currentLocation.activate(player)

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

    class Potion(Item):
        def __init__(self, id: int, name: str) -> None:
            super().__init__(id, name)
    
        def use(self, player: Type[Player]) -> None:
            player.add_health(amount=2)

    class Hint(Item):
        def __init__(self, id: int, name: str) -> None:
            super().__init__(id, name)
    
        def use(self, player: Type[Player]) -> None:
            print("The paper tells you to bring the clock to the attic.")


    ghostQuestions = QuestionHandler()
    zombieQuestions = QuestionHandler()
    sideQuest = QuestionHandler()
    finalBoss = QuestionHandler()
    goblinQuestions = QuestionHandler()
    gargoyleQuestions = QuestionHandler()
    ogreQuestions = QuestionHandler()
    ghostQuestion = Question("What's 1 + 1?", "2")
    ghostQuestion2 = Question("What's 2 + 3?", "5")
    ghostQuestion3 = Question("What's 5 + 4?", "9")
    ghostQuestion4 = Question("What's 10 - 7?", "3")
    ghostQuestion5 = Question("What's 6 + 6?", "12")
    zombieQuestion = Question("What's 42 in binary?", "101010")
    zombieQuestion2 = Question("What's 50 in binary?", "110010")
    zombieQuestion3 = Question("What's 100 in binary?", "1100100")
    zombieQuestion4 = Question("What's 21 in binary?", "10101")
    zombieQuestion5 = Question("What's 110100 in decimal?", "52")
    finalBossQuestion1 = Question("What year is it?", "2023")
    finalBossQuestion2 = Question("What is Obama's last name?", "Obama")
    finalBossQuestion3 = Question("Who the hell is Steve Jobs?", "Ligma Balls")
    finalBossQuestion4 = Question("What's the capital of Philippines?", "Manila")
    finalBossQuestion5 = Question("What planet do we live on?", "Earth")
    goblinQuestion = Question("What is the powerhouse of the cell?", "Mitochondria")
    goblinQuestion2 = Question("What does ATP stand for?", "Adenosine triphosphate")
    goblinQuestion3 = Question("What is the process by which plants create oxygen and water?", "Photosynthesis")
    goblinQuestion4 = Question("What do we call unicellular organisms?", "Prokaryotes")
    goblinQuestion5 = Question("What do we call multicellular organisms?", "Eukaryotes")
    gargoyleQuestion = Question("What is Alucard backwards?", "Dracula")
    gargoyleQuestion2 = Question("What are vampires weak to?", "Sunlight")
    gargoyleQuestion3 = Question("What is the worst vampire story ever told?", "Twilight")
    gargoyleQuestion4 = Question("What is the best vampire story ever told?", "Castlevania")
    gargoyleQuestion5 = Question("What is the inherited disorder where blood does not clot properly?", "Hemophilia")
    ogreQuestion = Question("Did Epstein kill himself?", "No")
    ogreQuestion2 = Question("What is your body's largest organ?", "Skin")
    ogreQuestion3 = Question("Which country invented tea?", "China")
    ogreQuestion4 = Question("Who painted the Mona Lisa?", "Leonardo Da Vinci")
    ogreQuestion5 = Question("What is the name of the blue Ninja Turtle?", "Leonardo")

    FBQs = [finalBossQuestion1,finalBossQuestion2,finalBossQuestion3,finalBossQuestion4,finalBossQuestion5]
    ghoQs = [ghostQuestion,ghostQuestion2,ghostQuestion3,ghostQuestion4,ghostQuestion5]
    zomQs = [zombieQuestion,zombieQuestion2,zombieQuestion3,zombieQuestion4,zombieQuestion5]
    gobQs = [goblinQuestion,goblinQuestion2,goblinQuestion3,goblinQuestion4,goblinQuestion5]
    garQs = [gargoyleQuestion,gargoyleQuestion2,gargoyleQuestion3,gargoyleQuestion4,gargoyleQuestion5]
    ogrQs = [ogreQuestion,ogreQuestion2,ogreQuestion3,ogreQuestion4,ogreQuestion5]
    ghostQuestions.add_questions(ghoQs)
    zombieQuestions.add_questions(zomQs)
    finalBoss.add_questions(FBQs)
    gargoyleQuestions.add_questions(garQs)
    goblinQuestions.add_questions(gobQs)
    ogreQuestions.add_questions(ogrQs)
    paperHint = Hint(4, "piece of paper")
    healthPotion = Potion(1, "potion")
    Clock = QuestItem(2, "ornate pocket watch")
    
    

    ghost = EnemyQuestion(1, "What seems to be a person flailing around under a blanket", 1, ghostQuestions)
    zombie = EnemyQuestion(2, "Somebody with terrible cuts all over their body", 1, zombieQuestions)
    lesserDemon = EnemyQuestion(3, "A disgusting humanoid presence lumbers towards and", 3, finalBoss)
    goblin = EnemyQuestion(4, "A small goblin", 1, goblinQuestions)
    gargoyle = EnemyQuestion(5, "A stone statue of a gargoyle", 1, gargoyleQuestions)
    ogre = EnemyQuestion(6, "A large ogre", 1, ogreQuestions)
    livingRoom.add_entity_on_location(ghost)
    kitchen.add_entity_on_location(zombie)
    attic.add_entity_on_location(lesserDemon)
    hiddenRoom.add_entity_on_location(goblin)
    secretTunnel.add_entity_on_location(gargoyle)
    treasureRoom.add_entity_on_location(ogre)
    hiddenRoom.add_item_on_ground(healthPotion)
    secretTunnel.add_item_on_ground(paperHint)
    treasureRoom.add_item_on_ground(Clock)

    secretEndingNPC = NPC(1, "Mysterious voice in the light", "Mysterious entity")
    secretEndingNPC.add_dialogue("All is not what it seems.")
    secretEndingReward = Item(4, "A cookie. Congratulations.")
    secretEndingQuest = Quest(questItem=Clock, rewardItem=secretEndingReward)
    secretEndingQuest.add_quest_dialogue("Time is gold. Bring the relic to me. \nIf you have thoroughly explored this place.")
    secretEndingNPC.set_quest(secretEndingQuest)
    secretEndingNPC.set_thanks_dialogue("I see you brought my pocket watch. Lol thanks here's a cookie.")
    attic.add_entity_on_location(secretEndingNPC)

game = Game(player=player)

# print(testQuestItem.id)

game.add_command("go", GoLogic())
game.add_command("use", UseLogic())
game.add_command("take", PickUpLogic())
game.add_command("inventory", CheckInventoryLogic())
game.add_command("talk", TalkLogic())

if __name__ == '__main__':
    playerName = str(input("Welcome to...\n---------------\nW A K E  U P !\nA text-based RPG\n---------------\nWhat is your name, young one? "))
    player.set_name(playerName)
    print("I see, nice to meet you {}!".format(player.get_name()))
    game.run()

game.run()
