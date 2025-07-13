used with chat or in game. can send a deal that the other player can accept or reject. 
  Scenario: Player sends a deal
    Given a player has sent a deal to another player
    When the other player receives the deal
    Then they can accept or reject the deal

  Scenario: Player accepts a deal
    Given a player has received a deal
    When they accept the deal
    Then the deal is finalized and both players are notified

  Scenario: Player rejects a deal
    Given a player has received a deal
    When they reject the deal
    Then the deal is discarded and both players are notified

  Scenario: Player negotiates a deal
    Given two players are negotiating a deal
    When they exchange terms and conditions
    Then they can reach an agreement or walk away from the negotiation