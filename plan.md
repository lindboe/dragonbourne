

## Features in both modes
 * directories represent locations
   * must travel through all directories to get from one location to another, but can specify a location to "jump" to (the implication is just that each location on the way was traveled through
   * player always has a "home" directory where they are "safe" from harm, can bank items, and return here if died
 * multiplayer support (perhaps only play mode, actually?)
   * fight together, trade, steal, talk with other players
   * "follow" command to stick with another user and let them lead?
   * locate other players either by character name or system username
 * ability to create locations and NPCs with yaml templates (and possibly also customize attributes/actions)
 * have multiple "games" for multiple template sets, perhaps even multiple characters for one template set

## Work mode
 * non-destructive: no editing files or changing perms except those that this program laid down itself
 * monsters are more rare
 * no action will take place without the user taking action first (eg, monsters will never attack first)
 * XP awarded for running common bash commands too: this is explained in the form of a story
   * would be neat to add user-specific common commands to a "spellbook" and incorporate them
 * interesting locations/NPCs/stores(?) scattered randomly or available on demand?

## Play mode
 * set a specific dir tree to play in
    * when traveling along a dir path, even when "jumping", can be stopped by an event/character
    * should pause/quit with warning if user attempts to navigate out of specified tree or home dir

## Characters

### Base stats
 * HP
 * XP
 * str
 * def

### Basic attributes
 * character name
 * character description
 * character home (defaults to player's home dir - this could present problems for Play Mode if home dir is not in subdirectory)

### The backpack
 * each character, playable and not, owns a backpack where items in their possession are stored
 * max (15? 20?) items

### The player character

### NPCs

#### Monsters

## Items

* all items should have the following actions available
  * `use`
  * `examine` (which has the synonym `look at`)

### Wearables

 * `wear` (synonyms: don, put on, equip, wield)

#### Weapons

### Food/drink

 * `consume` (synonyms: eat, drink, ingest)

## Buy/Sell/Trade/Give/Steal

 * both parties must acquiesce to trade
   * NPCs evaluate fairness of a trade by... assigned monetary or rarity value on item? Item "strength"?
 * giving can happen without second party's consent if there is room in backpack
   * if there is not, need a "drop" option
 * stealing is very difficult
   * will usually fail, will sometimes notify victim on failure
   * NPC reaction to theft?
   * Can users see each other's backpack?

## Combat

Turn-based? how will this work with multiple players?
Choosing which weapon/attack type to use?
Unarmed combat?

### Death

If a player character dies, they will be sent back to their home directory with HP restored. (Penalty...?)
If an NPC dies...? Possibility of revival?
