# Dungeons & Damage
<p>This is an experimental rpg that will get updated as time goes on</p>
<p>It's meant to be a space to put things we've learned to the test as we learn more things in Python</p>
<p>As of this release, I don't really have an idea as to where I should go from here. I don't want to add visuals, as the terminal is much more unique</p>
<p>Also, it's kinda just Excalibur on this right now. Emilio isn't in Python 2 and went to go take game design. I hope he comes back with the ability to make this game better.</p>
<p>It started as a fun little thing and as of now is evolving</p>

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
<p>I want to add a new gun interaction, where if you missed your shot, the narrator will remember that and laugh whenever the next gun comes into play</p>
<p>Abilites for each character are in the works, and right now each fighter has a very simple passive ability that won't determine the outcome of the match</p>
<p>A computer. Idk how this would work, and it would probably be a lot of if statements and easily exploitable.</p>
<p>More magic options maybe?</p>
<p>More than 2 players. I think this would be cool. Maybe a 4-player FFA</p>
<p>Or maybe a 2v2 mode where you can cast benificial spells for allies</p>
<p>I like how this is becoming closer to Pokemon with every update</p>

<p>⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️</p>

## Character Stats:

### Stat Descriptions:
<p>HP: Health Points. This goes to 0, you lose the game.</p>
<p>ATK: Attack Damage. This is how much damage you do on a sucessful hit.</p>
<p>atkBON (ATK(FOUND HERE)): Attack Roll Bonus. This is what is added to the random 1-20 number when determining a hit</p>
<p>DEF: Defence. When you are attacked, this number is compared to a random number (1-20) plus their atkBON</p>
<p>MP: Magic Points/Power: Determines how much magic you can use. Different spells cost different amounts of MP</p>
<p>mpBON (MP(FOUND HERE)): Magic Point/Power Refresh. At the end of each turn, you get this much MP back</p>
<p>SPD: Speed. When determining who goes first, it is determined by whoever has the highest speed</p>
<p>ItUs: Item Uses. Each character can use a certain amount of items on their turn, being the value of ItUs (it's not actually that in the code)</p>

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
<p>Coder - Excalibur</p>
<p>Coder - Emilio</p>
<p>Teacher - Mr. Young</p>
<p>Assistant Teacher - CodeHS</p>
