how the game starts, players can choose to play as different factions with unique abilities and characteristics.
  Scenario: Player selects a faction
    Given a player is starting a new game
    When they select a faction
    Then the game initializes with the selected faction's attributes

  Scenario: Player starts a new game
    Given a player has selected a faction
    When they start the game
    Then the game board is set up and the player is ready to play

  Scenario: Player joins an existing game
    Given a player wants to join an existing game
    When they select the game to join
    Then they are added to the game and can start playing

  Scenario: Player leaves a game
    Given a player is in an ongoing game
    When they choose to leave the game
    Then they are removed from the game and cannot take further actions