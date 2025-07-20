# KISS - Game Design Document

## Table of Contents
1. [Game Overview](#game-overview)
2. [Core Systems](#core-systems)
3. [Leader System](#leader-system)
4. [Combat System](#combat-system)
5. [Diplomacy System](#diplomacy-system)
6. [Movement & Map](#movement--map)
7. [Resources & Economy](#resources--economy)
8. [Artifact System](#artifact-system)
9. [Victory Conditions](#victory-conditions)
10. [Turn Sequence](#turn-sequence)
11. [Game Setup](#game-setup)
12. [Examples](#examples)

---

## Game Overview

### Theme & Setting
10,000 years ago, an evil empire conquered the galaxy, suppressing all technology and preventing anyone from leaving their homeworlds. Over time, the empire's power crumbled due to internal strife and paranoia. A civil war broke out, and suddenly the empire was gone - their forces scattered and confused. Now is the time when everyone is racing to claim freedom and build their own empires before any remnant of the old order can return.

### Core Concept
KISS is a strategic empire-building game where players expand across a 32x32 sector galaxy, managing leaders who provide crucial bonuses but can defect to other players. The game focuses on survival - the last player with their main leader alive wins.

### Design Philosophy
- **Simplicity:** All mechanics use 1-5 scales and simple dice rolls
- **Strategic Depth:** Leader loyalty and diplomacy create complex decisions
- **Personal Stakes:** Every leader matters, every decision has consequences
- **Dark Infographic Aesthetic:** Clean, professional UI that looks like an analytics dashboard

---

## Core Systems

### Scale & Scope
- **Map Size:** 32x32 sectors (1,024 total)
- **Scale:** Each sector = 1 light-year across
- **Player Count:** 4-8 players
- **Game Length:** Variable (elimination-based victory)

### Fundamental Mechanics
- **Core Resolution:** D6 - D6 system (range -5 to +5)
- **Bonus System:** All bonuses are whole numbers (+1 to +5)
- **Resource Scale:** Everything rated 1-5 for consistency
- **Mental Math:** Players can calculate odds in their head

---

## Leader System

### Leader Basics
- **Maximum Leaders:** 5 per player
- **Player Leadership Rating:** 1 + number of recruited leaders (max 5)
- **Leader Bonuses:** +1 to +5 (affects combat and other actions)
- **Influence Range:** Leaders affect sectors equal to their bonus value

### Leader Types
1. **Military Leaders:** Provide combat bonuses to fleets
2. **Industrial Leaders:** Boost resource production on worlds
3. **Explorer Leaders:** Increase movement range and exploration benefits

### Leader Loyalty & Defection
- **Loyalty Factors:** Equipment quality, success rate, treatment
- **Defection Triggers:** Better offers from enemies, poor treatment, failures
- **Defection Consequences:** Leader takes assets equal to their rating
  - Military: Ships worth their leadership rating in tech levels
  - Industrial: Resources equal to their leadership rating
  - Explorer: Reveals sectors equal to their leadership rating

### Leader Recruitment
- **Sources:** Conquered inhabited worlds, diplomatic recruitment
- **Discovery Rate:** D6 roll when conquering worlds
  - 1-2: No leader present
  - 3-4: Minor leader (+1 or +2 bonus)
  - 5-6: Major leader (+3 or +4 bonus)

---

## Combat System

### Ship Types & Values
1. **Corvette (T:1):** Fast, cheap, weak
2. **Destroyer (T:2):** Balanced ship type
3. **Cruiser (T:3):** Heavy combat vessel
4. **Battleship (T:4):** Powerful capital ship
5. **Kaiju (T:5):** Ultimate warship

### Combat Resolution
1. **Calculate Fleet Values:** Add up all ship tech levels
2. **Determine Bonus:** Higher fleet value ÷ lower fleet value (round down)
3. **Add Leader Bonuses:** Max +5 total, +1 if leader present in battle
4. **Roll:** D6 + bonuses - D6 + bonuses
5. **Apply Damage:** Difference = damage points

### Damage Application
- **Priority:** Largest ships destroyed first
- **Cascade:** If no ships of exact size, damage flows to smaller ships
- **Examples:**
  - 7 damage vs 2 T:5 ships = 1 T:5 destroyed, 1 survives
  - 7 damage vs 4 T:2 ships = 3 T:2 destroyed, 1 survives
  - 7 damage vs 7 T:1 ships = all destroyed

### Resource Costs
- **Combat Cost:** 1 resource per ship per battle (win or lose)
- **Retreat Cost:** 1 resource per ship (positioning/maneuvering)
- **Strategic Implication:** High-tech ships are resource-efficient

---

## Diplomacy System

### Diplomatic Actions
When encountering any sector, players choose:
1. **Attack:** Standard combat resolution
2. **Flee:** Retreat (both sides pay resource costs)
3. **Diplomacy:** Attempt leader recruitment

### Recruitment Mechanics
1. **Leadership Clash:** D6 + Your Leadership vs D6 + Target Leadership
2. **Gift Enhancement:** Offer appropriate gifts for bonus
   - Military Leaders: Ships (bonus = tech level difference, max +5)
   - Industrial Leaders: Resources (bonus = resources offered, max +5)
   - Explorer Leaders: Artifacts (bonus = artifact value, max +5)
3. **Gift Evaluation:**
   - Better gift = positive bonus
   - Equal gift = no bonus
   - Worse gift = +1 "insult" bonus to resist

### Protection Through Equipment
- **Well-Equipped Leaders:** Harder to recruit away
- **Natural Defense:** Good equipment creates insult bonuses
- **Strategic Investment:** Players must balance equipment allocation

### Leader Slot Management
- **Full Roster (5 leaders):** New stronger leaders replace weaker ones
- **Absorption:** Weaker leaders disappear into empire
- **Defense Bonus:** Leaders being "absorbed" get bonus equal to player's leadership rating

---

## Movement & Map

### Movement System
- **Base Movement:** 2 sectors per turn for all ships
- **Explorer Bonus:** +1 sector (3 total) for fleets with Explorer leaders
- **Artifact Enhancement:** Ancient Navigation cards provide +1 sector for one jump

### Map Generation
- **Standard Sectors:** Star systems with R:1-3, T:1-2
- **Empty Sectors:** No resources or defenses
- **Special Sectors:** ~60 total across map
  - Gravity wave areas
  - Machine worlds
  - Artifact sites
  - Other anomalies (R:1-5, T:1-5)

### NPC Defenses
- **Defense Formula:** Ships = Resource rating, Tech = Planet tech level
- **Example:** R:3, T:2 world has 3 T:2 ships + 3 resources for combat
- **Resources:** NPCs spend resources to defend (1 per ship per battle)

---

## Resources & Economy

### Resource System
- **Single Resource Type:** "Production" (represents materials, food, manufacturing)
- **Generation:** Planets produce resources equal to their R: rating each turn
- **Usage:** Ship construction, combat costs, upgrades, gifts

### Planet Development
- **Resource Rating (R:):** 1-5 (resources produced per turn)
- **Tech Level (T:):** 1-5 (defensive capability, construction cost)
- **Upgrade Cost:** Tech level = resources required
- **Build Time:** Tech level = turns to complete
- **Upgrade Choice:** Extract resources OR upgrade tech level each turn

### Construction Costs
- **Ships:** Cost = tech level (T:3 ship costs 3 resources)
- **Upgrades:** Cost = target tech level (upgrade to T:4 costs 4 resources)
- **Time:** Construction time = tech level

---

## Artifact System

### Artifact Distribution
- **Quantity:** ~60 artifacts scattered across 1,024 sectors
- **Discovery:** First fleet to reach artifact site claims it immediately
- **Usage:** One-time effects played during appropriate phases

### Artifact Types
1. **Ancient Fuel Depot:** Roll 1D5, gain that many resources
2. **Quantum Amplifier:** +2 bonus to ONE combat roll this turn
3. **Ancient Shipyard:** Roll 1D5, build ship of that size instantly
4. **Stealth Generator:** Roll 1D5, negate that much damage in one battle
5. **Holo Projector:** Roll 1D5, add that many temporary ships to fleet
6. **Ancient Navigation:** One fleet can move +1 sector this turn

### Strategic Value
- **Risk vs Reward:** Rushing for artifacts may leave fleets vulnerable
- **Tactical Timing:** When to play cards for maximum effect
- **Diplomatic Currency:** Artifacts can be gifted to recruit leaders

---

## Victory Conditions

### Elimination Victory
- **Win Condition:** Last player with their main leader alive
- **Elimination:** Player is eliminated when their main leader is killed/captured
- **Natural Collapse:** Players may be eliminated through leader defections and resource starvation

### Survival Challenge
- **Core Question:** "How long can you hold your empire together?"
- **Multiple Failure States:**
  - Military defeat (leader killed in battle)
  - Internal collapse (too many leader defections)
  - Resource starvation (can't maintain forces)
  - Diplomatic isolation (all other players allied against you)

---

## Turn Sequence

### Step 0: Artifact Phase
- Play any artifact cards for immediate effects

### Step 1: Resource & Allocation Phase
**1a. Resource Generation**
- All planets generate resources equal to their R: rating

**1b. Resource Allocation**
- Player distributes total resources among leaders/projects

**1c. Planet Actions**
- Choose: Generate resources OR Spend resources (upgrade/build)
- Continue in-progress construction projects

### Step 2: Initiative & Movement
- **Initiative Roll:** D6 + bonuses (smaller empires get +1)
- **Winner moves first:** Claims territory and artifacts
- **Loser moves second:** Responds tactically

### Step 3: Claims Resolution
**3a. Claim Unclaimed Sectors/Planets**
- If only one player present, automatic claim
- If contested, no automatic claim

**3b. Artifact Claims**
- First fleet to arrive claims artifact immediately
- Subsequent arrivals fight for control of sector

### Step 4: Combat Resolution
- Resolve all battles in contested sectors
- Apply fight/flee/diplomacy choices
- Process leadership contests for recruitment

### Step 5: Damage & Leader Management
**5a. Apply Damage**
- Destroy ships based on combat results
- Apply leader loss penalties if leaders died

**5b. Leader Repositioning**
- Leaders can move to other ships/sectors within range
- Leader abandonment may cause morale penalties

### Step 6: Capture Resolution
- Planets reduced to T:0 are captured
- New owner takes control next turn

---

## Game Setup

### Map Generation
1. **Generate 32x32 grid** (1,024 sectors)
2. **Roll for sector contents** based on population density
3. **Place ~60 special locations** (artifacts, anomalies)
4. **Place 8-12 Empire remnant factions** (2-4 sectors each)

### Player Starting Conditions
**Every Player Starts With:**
- **Homeworld:** R:5, T:1 (excellent production, minimal defense)
- **Fleet:** 5 T:1 ships (Corvettes)
- **Resources:** 5 stored resources
- **Leader:** Yourself only (no additional leaders)
- **Vision:** Full information on sectors within 2 sectors of homeworld

### Starting Positions
- **Placement:** Random with minimum 10 sectors between players
- **Rationale:** Ensures expansion room before player contact
- **Balance:** No player starts at map edges

### Leadership Specialization
**Choose at game start:**
1. **Military Commander:** +1 to all combat rolls
2. **Industrial Leader:** +1 resource generation per turn (empire-wide)
3. **Explorer:** +1 movement range for all fleets

---

## Examples

### Example Combat
**Scenario:** 4 T:3 Cruisers attack 2 T:1 Corvettes + 1 T:4 Battleship

**Fleet Values:**
- Attacker: 4 × 3 = 12 points
- Defender: (2 × 1) + (1 × 4) = 6 points

**Combat Bonuses:**
- Attacker: +2 (12÷6=2) + 3 (leader) = +5 total
- Defender: +1 (leader) = +1 total

**Battle:**
- Attacker: D6 + 5 = (rolls 3) = 8
- Defender: D6 + 1 = (rolls 4) = 5
- **Result:** Attacker wins by 3

**Damage Application:**
- 3 damage to defender
- T:4 Battleship destroyed (4 damage needed, but only 3 available)
- Battleship survives, both Corvettes destroyed

### Example Diplomacy
**Scenario:** Player (L:2) attempts to recruit enemy L:3 Military Leader who has 2 T:4 ships

**Gift Evaluation:**
- Player offers 1 T:2 ship
- Target has T:4 ships (better equipment)
- Target gets +1 "insult" bonus for inferior gift

**Recruitment Roll:**
- Player: D6 + 2 = (rolls 5) = 7
- Target: D6 + 3 + 1 = (rolls 2) = 6
- **Result:** Player wins by 1, leader defects!

**Asset Transfer:**
- L:3 Military Leader joins player
- Takes 1 T:3 ship (or equivalent) when defecting
- Remaining T:4 ship stays with original owner

### Example Turn Sequence
**Turn 3 Example:**

**Step 0:** Player A plays Ancient Fuel Depot, rolls 4, gains 4 resources

**Step 1:** 
- All planets generate resources
- Player A allocates 8 resources to military leader, 5 to expansion
- Planet Xerion chooses to upgrade from T:2 to T:3 (costs 3 resources)

**Step 2:**
- Initiative: Player A rolls 4, Player B rolls 6
- Player B moves first, sends fleet to artifact site
- Player A moves second, intercepts at artifact site

**Step 3:**
- Player B claims artifact (arrived first)
- Both fleets now in same sector (contested)

**Step 4:**
- Combat: Player A chooses Attack, Player B chooses Fight
- Battle resolved, Player A wins
- Player B's fleet destroyed, but they keep the artifact

**Step 5:**
- No leaders lost, no repositioning needed

**Step 6:**
- No planets captured this turn

---

## Design Notes

### Balance Considerations
- **High-tech ships are powerful but expensive** (resource efficiency vs raw power)
- **Leaders provide crucial bonuses but can defect** (risk vs reward)
- **Diplomacy can steal leaders but requires investment** (gifts can be lost)
- **Initiative provides advantages but alternates** (no permanent advantage)

### Scalability
- **4 players:** Intimate, tactical gameplay
- **8 players:** Epic, diplomatic gameplay
- **Turn time scales with simultaneous phases**
- **Leader AI can handle slow players**

### Future Expansions (Tier 1+)
- **Complex artifacts** with multiple effects
- **Technology trees** for ship advancement
- **Alliance mechanics** for cooperative play
- **Empire remnant interactions** as ongoing threats
- **Leader personality traits** affecting behavior
- **Resource storage limits** for economic pressure

---

## Victory Examples

### Military Victory
Player systematically eliminates opponents through superior fleet management and combat tactics, keeping leaders well-equipped and loyal while destroying enemy leaders in battle.

### Diplomatic Victory
Player recruits key enemy leaders through superior gifts and timing, causing enemy empires to collapse from internal defections, then eliminates weakened opponents.

### Survival Victory
Player focuses on defensive play and leader loyalty, outlasting more aggressive opponents who overextend and lose their leaders to combat or defection.

### Economic Victory
Player builds massive resource production, uses wealth to maintain leader loyalty and recruit new leaders, eventually overwhelming opponents through sheer economic power.

---

*End of Game Design Document*
