import { Ship, LeaderType } from './index';

export interface Leader {
  id: string;
  type: LeaderType;
  name: string;
  skillLevel: number;
  fleetId: string;
}
export interface LeaderWithShips extends Leader {
  ships: Ship[];
}