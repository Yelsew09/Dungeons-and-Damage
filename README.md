# Dungeons & Damage
<p>Originally, this was a space for me and a friend to make things during our Python 1 class at school, as we were bored out of our minds.</p>
<p>This project was good enough that when the final project came around all I had to do was implement classes and the custom character.</p>
<p>I don't remember the details, but I think it needed to consist of a class-based custom character creator with an inventory system.</p>
<p>Emilio had already implemented the inventory system, aka the items, and I took that and made it fit into the program to have it work for the project. I don't know if Emilio used that version as his project.</p>
<p>Python 2 rolled around, and Emilio hadn't taken the class, so I was on my own. I learned how to make a website with Django in that class, however I've forgotten how to use it now.</p>
<p>During my time in Python 2, I wanted to learn c++, as I had learned that's what most game devs use. At the time, I had no idea what "memory management" was, but I was ready to learn.</p>
<p>About 2 weeks later, I was confident in my ability to use the language at the most basic level. I was not, and I'll talk about that more in the c++ release.</p>
<p>For a while, I was still adding some new things to the Python version, but as I got deeper into the c++ wormhole, the Python version was left in the dust</p>
<p>The Python version is still in that state, as I have decided to add visuals. I intitally just googled "easy c++ visual library".</p>
<p>This introduced me to Raylib, and then I had a nightmare the following night where I kept failing to find and implement the best verion of it. Would that be the quickstart? The master branch?</p>
<p>Wait, no, that actually happened.</p>
<p>Raylib is still great, and I would reccomemd using it if you can set it up in the way you'd like.</p>
<p></p>
<p>Enter OpenGL, what Raylib is based in. You need like, 200 lines of code to render one orange triangle (not including everything in #include).</p>
<p>So that's the state I'm in. The base c++ version is being worked on in school, because GitHub codespaces are availible on the school-provided laptops, but it doesn't support a $DISPLAY_ENVIROMENT, so I can't see visuals. I can still code things, but I can't see what it looks like. The OpenGL version is not being worked on, because I'm still struggling to understand what a VAO is. I think I'm getting close, though.</p>
<p>Around Late Augest/Early September of 2025, I joined my school's robotics team. So, I learned Java for that.</p>
<p>And now, I'm working on a Java version of this game. It's not going to be ready any time soon.</p>
<p>Further information on each version can be found on the corrosponding branch</p>

## Characters
<p>You can play as:</p>

### Knight
<p>A man who fought valiantly and for honor for his kingdom. Now, he’s been captured and put to fight in the arena. If he wins, he will be allowed to leave.</p>

### Peashooter
<p>No one knows how he came to be. He’s a plant that shoots peas out of his mouth. Some say he was made by a witch, others, god. No one knows, not even him</p>

### Mage
<p>A traveling mage who claims to have mastered magic as a whole. People were skeptical, so he decided to go to the gladiator fight and prove that he is a master of all things arcane</p>

### Rouge
<p>The rouge was caught stealing from the King. Because of this, the King sent the rouge to fight in the gladiator fight, one that he would be attending personally. If the rouge put on a good show, he and his family would get rewarded handsomely (only the family if he dies), and if he doesn’t, he will be executed</p>

### Skele
<p>One day, a pile of bones in a prisoner cell became animated. The people in charge of the prison saw this and thought, “Hey! Why don’t we just send him into the arena if he can’t die?”</p>

### Bard
<p>The bard is a barkeep at the local bar. He serves drinks, he plays songs, and he gets to know the regulars. One day, he made a bet with someone where the loser would go fight in the arena. Needless to say, he lost the bet</p>

### Barbarian
<p>The barbarian has no identity, so we can’t really give him a proper story, but he kinda just broke in to the arena for the thrill of the fight</p>

### -.- --- -. .- -- .. ....... -.-. --- -.. .
<p>.. ... ....... .- ....... .-.. .. - . .-. .- .-.. ....... --. --- -..</p>
<p>.- .-.. .-.. ....... --- ..-. ....... .... .. ... ....... ... - .- - ... ....... .- .-. . ....... ---.. ---.. ..--- ..--- ....- -.... ....- -.... --... ----. ----- --..-- ....... .-- .... .. -.-. .... ....... .. ... ....... - .... . ....... -.- --- -. .- -- .. ....... -.-. --- -.. . ....... --- -. ....... - .... . ....... -.- . -.-- .--. .- -..</p>

# Plans
- [ ] First things first, the c++ version must be released
- [ ] I also need to extensively bug test the Python version becasuse I know there's some issues
- [ ] I want to increase the maximum number of players in some way to 4. This will end up being a 2v2 or FFA
- [ ] A story mode. Emilio has somewhere to start on this, and a sentence or 2 has already been written about each of the characters
- [ ] Sliced Bread or smth idk

<p>⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️</p>

## Character Stats:

### Stat Descriptions:
<p>hp: Health Points. This goes to 0, you lose the game.</p>
<p>atk: Attack Damage. This is how much damage you do on a sucessful hit.</p>
<p>atkBON (ATK(FOUND HERE)): Attack Roll Bonus. This is what is added to the random 1-20 number when determining a hit</p>
<p>def: Defence. When you are attacked, this number is compared to a random number (1-20) plus their atkBON</p>
<p>mp: Magic Points/Power: Determines how much magic you can use. Different spells cost different amounts of MP</p>
<p>mpBON (MP(FOUND HERE)): Magic Point/Power Refresh. At the end of each turn, you get this much MP back</p>
<p>itus: Item Uses. Each character can use a certain amount of items on their turn, being the value of item_uses</p>
<p>spd: Speed. Turn order is determined by speed stats. The higher speed stat player goes first. In the event of a tie, the person who goes first is chosen randomly. That will then be the turn order for the rest of the game</p>


### Knight stats:
    HP: 35  ATK: 7(+5)  DEF: 16  MP: 5(+3)  SPD: 3  ItUs: 2
    Passive: Fortitude. -2 Damage taken

### Peashooter stats:
    HP: 26  ATK: 9(+4)  DEF: 14  MP: 7(+3)  SPD: 5  ItUs: 3
    Passive: Charge. For every turn ended at maxMP, add 2 to your next attack

### Rouge stats:
    HP: 20  ATK: 10(+3)  DEF: 13  MP: 6(+2)  SPD: 4  ItUs: 4
    Passive: Accelerate. After every turn, increase your speed by 1 (max 7), and your attack roll bonus by 1 (max 9)

### Mage stats:
    HP: 21  ATK: 5(+2)  DEF: 11   MP: 5(+2)  SPD: 4  ItUs: 2
    Passive: Zoning In. After every turn, increase your maximum MP by 1 (max 10), and set your MP refresh to 1/2 of your maximum MP

### Skele stats:
    HP: 30  ATK: 7(+3)  DEF: 12  MP: 7(+5)  SPD: 6  ItUs: 4
    Passive: Focused. Cannot take more than 14 damage in a single hit (excluding instant kills)

### Bard stats:
    HP: 27  ATK: 6(+4)  DEF: 14  MP: 4(+2)  SPD: 2  ItUs: 5
    Passive: Jack of All Trades. After every turn, you may switch to a different set of stats (as long as it won't kill you)

### Barbarian stats:
    HP: 40  ATK: 12(+2)  DEF: 15  MP: 2(+1)  SPD: 1  ItUs: 1
    Passive: Healthy. Heal 3 damage after every turn, and get 1.5x to any healing

## Spells:
<p>Fireball - 5MP: Does an amount of damage between your maximum MP and 1.5x your maximum MP. Can be blocked if the magic is too weak</p>
<p>Summon Random Item - 2MP: Adds a random item to your inventory. Different items have different chances of appearing</p>
<p>Gain Advantage - 3MP: Give yourself advantage, even if you had disadvantage</p>
<p>Impose Disadvantage - 4MP: Remove the other player's advantage, or give them disadvantage</p>
<p>Heal 20% - 4MP: Heals 20% of your maximum HP</p>
<p>Damage Boost - 2MP: Add 1/3 of your ATK to your next attack, hit or miss</p>

## Items:
<p>Note - the % is the chance of appearing from the Summon Random Item spell</p>
<p>Rusty Spoon - 10%: Do 1 point of unblockable damage. Has a .1% chance to kill either player instantly from tetanus</p>
<p>Knives - 40%: Do 1-5 points of unblockable damage, with a 1/10 chance to miss</p>
<p>Healing Potion - 40%: Heal 10% of your maximum HP</p>
<p>Chain Link Fence - 10%: Block one hit, regardless of damage</p>

## Credits
<p>Coder - Splitfish</p>
<p>Coder - Emilio</p>
<p>Teacher - Mr. Young</p>
<p>Assistant Teacher - CodeHS</p>
<p>Online Resource - W3schools.com</p>
<p>Online Resource - GeeksforGeeks.org</p>
