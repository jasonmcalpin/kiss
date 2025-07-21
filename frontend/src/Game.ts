import { createUniverse } from './components/game/creation/UniverseCreation';


export class Game {
  constructor() {
    this.universe = null;
  }

  async createUniverse(data) {
    try {
      const response = await createUniverse(data);
      if (response.success) {
        this.universe = response.universeId;
        console.log(`Universe created with ID: ${this.universe}`);
      } else {
        console.error(`Failed to create universe: ${response.message}`);
      }
    } catch (error) {
      console.error('Error creating universe:', error);
    }
  }
}
