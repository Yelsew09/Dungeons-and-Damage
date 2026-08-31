# Dungeons & Damage

This is an experimental rpg that will get updated as time goes on

It's meant to be a space to put things we've learned to the test as we learn more things in Python

As of this release, I don't really have an idea as to where I should go from here. I don't want to add visuals, as the terminal is much more unique

Also, it's kinda just Excalibur on this right now. Emilio isn't in Python 2 and went to go take game design. I hope he comes back with the ability to make this game better.

It started as a fun little thing and as of now is evolving

Speaking of evolving, this is being written god knows how long later. I'm sitting here at the start of my senior year and Emilio hasn't come back to this. He isn't even in Game Design 2. So I became self-taught C++. I learned more of that than I did French in French class. I also became self-taught Java, I had to in order to code for Robotics Club, but at the end of the day no one chooses to code in Java. JS, maybe, but not Java. The main motivation of this was because C++ is just the best coding language for games. It's not a debate. So, what better to test this than a full recode of this game in C++ from the ground up and maybe with a couple more features.

## Characters

You can play as:

### Knight

    A man who fought valiantly and for honor for his kingdom. Now, he’s been captured and put to fight in the arena. If he wins, he will be allowed to leave.

### Peashooter

    No one knows how he came to be. He’s a plant that shoots peas out of his mouth. Some say he was made by a witch, others, god. No one knows, not even him

### Mage

    A traveling mage who claims to have mastered magic as a whole. People were skeptical, so he decided to go to the gladiator fight and prove that he is a master of all things arcane

### Rouge

    The rouge was caught stealing from the King. Because of this, the King sent the rouge to fight in the gladiator fight, one that he would be attending personally. If the rouge put on a good show, he and his family would get rewarded handsomely (only the family if he dies), and if he doesn’t, he will be executed

### Skele

    One day, a pile of bones in a prisoner cell became animated. The people in charge of the prison saw this and thought, “Hey! Why don’t we just send him into the arena if he can’t die?”

### Bard

    The bard is a barkeep at the local bar. He serves drinks, he plays songs, and he gets to know the regulars. One day, he made a bet with someone where the loser would go fight in the arena. Needless to say, he lost the bet

### Barbarian

    The barbarian has no identity, so we can’t really give him a proper story, but he kinda just broke in to the arena for the thrill of the fight

### Limit

    This is the result of pushing the coding to the absolute limit. The way to access this character is kept secret

## Plans

- [ ] I want to add a new gun interaction, where if you missed your shot, the narrator will remember that and laugh whenever the next gun comes into play

- [ ] Abilites for each character are in the works, and right now each fighter has a very simple passive ability that (hopefully) won't automatically determine the outcome of the match

- [ ] A computer. Idk how this would work, and it would probably be a lot of if statements and easily exploitable.

- [ ] More magic options maybe?

- [ ] More than 2 players. I think this would be cool. Maybe a 4-player FFA, or maybe a 2v2 mode where you can cast benificial spells for allies

I like how this is becoming closer to Pokemon with every update

⚔️

## Character Stats

### Stat Descriptions

HP: Health Points. This goes to 0, you lose the game.

ATK: Attack Damage. This is how much damage you do on a sucessful hit.

atkBON (ATK(FOUND HERE)): Attack Roll Bonus. This is what is added to the random 1-20 number when determining a hit

DEF: Defence. When you are attacked, this number is compared to a random number (1-20) plus their atkBON

MP: Magic Points/Power: Determines how much magic you can use. Different spells cost different amounts of MP

mpBON (MP(FOUND HERE)): Magic Point/Power Refresh. At the end of each turn, you get this much MP back

SPD: Speed. When determining who goes first, it is determined by whoever has the highest speed

ItUs: Item Uses. Each character can use a certain amount of items on their turn, being the value of ItUs (it's not actually that in the code)

### Knight stats

    HP: 35  ATK: 6(+5)  DEF: 16  MP: 5(+3)  SPD: 3  ItUs: 2

Passive: Endure. -2 Damage taken (minimum of 0)

Activated: Smite the Pathetic - 3 turn cooldown. Your next basic attack deals additional damage equal to your MP at the time of use. This does not end your turn

### Peashooter stats

    HP: 26  ATK: 9(+4)  DEF: 14  MP: 7(+3)  SPD: 5  ItUs: 3

Passive: Charge. For every turn ended at > 1/2 mpMAX, add 2 to your next attack

Activated: Photosythesis B*tch - 5 turn cooldown. Heal damage equal to your current amount of MP each turn until you get damaged. Ends your turn, cooldown starts after reaching full HP or after taking damage

### Rouge stats

    HP: 20  ATK: 10(+3)  DEF: 13  MP: 6(+2)  SPD: 7  ItUs: 4

Passive: Evade. If a spell's damage is below SPD + atkBON, halve the damage

Activated: Nuh uh - 5 turn cooldown. Evade procs on the next damage you take

### Mage stats

    HP: 21  ATK: 5(+2)  DEF: 11   MP: 5(+2)  SPD: 4  ItUs: 2

Passive: Hone. After every turn, increase your maximum MP by 1 (max 10), and set your MP refresh to 1/2 of your maximum MP

Activated: I don't care how big the room is - 7 turn cooldown. Cast Fireball for free

### Skele stats

    HP: 30  ATK: 7(+3)  DEF: 12  MP: 7(+5)  SPD: 6  ItUs: 4

Passive: Focus. Cannot take more than 14 damage in a single hit (excluding instant kills)

Activated: Dry Bones - 8 turn cooldown. Until the end of your next turn, you are inactionable and invulnurable

### Bard stats

    HP: 27  ATK: 6(+4)  DEF: 14  MP: 4(+2)  SPD: 2  ItUs: 5

Passive: Adapt. After every turn, you may switch to a different set of stats (as long as it won't kill you)

Activated: 1d4 Psychic Damage - 3 turn cooldown. Deal 1d4 magic damage and give your opponent disadvantage on their next attack

### Barbarian stats

    HP: 40  ATK: 12(+2)  DEF: 15  MP: 2(+1)  SPD: 1  ItUs: 1

Passive: Regenerate. Heal 3 damage after every turn, and get 1.5x to any healing (included in passive regen)

Activated: Rage - 7 turn cooldown. Until the end of your next turn, you get +2 to atkBON and take .5x damage

## Spells

Fireball - 5MP: Does an amount of damage between your maximum MP and 1.5x your maximum MP. Can be blocked if the magic is too weak

Summon Random Item - 2MP: Adds a random item to your inventory. Different items have different chances of appearing

Advantage - 3MP: Give yourself advantage, even if you had disadvantage

Disadvantage - 4MP: Remove the other player's advantage, or give them disadvantage

Heal - 4MP: Heals 20% of your maximum HP

Damage Boost - 2MP: Add 1/3 of your ATK to your next attack, hit or miss

## Items

### Note - the % is the chance of appearing from the Summon Random Item spell

Rusty Spoon - 10%: Do 1 point of unblockable damage. Has a 1/1000 chance to kill either player instantly from tetanus

Knives - 40%: Do 1-5 points of unblockable damage, with a 10% chance to miss

Healing Potion - 40%: Heal 10% of your maximum HP

Chain Link Fence - 10%: Block one hit, regardless of damage

## Credits

### C++ Version

Coder - Excalibur

Online Resource - GeeksforGeeks

Online Resource - W3Schools

### Python Edition

Teacher - Mr. Young

Online Resource - CodeHS
