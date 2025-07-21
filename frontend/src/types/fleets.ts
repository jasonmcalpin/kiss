import { ShipType, TechLevel, ResourceRating, LeadershipRating } from './index';

export interface Fleet {
  id: string;
  ships: Ship[];
}
export interface Ship {
  id: string;
  type: ShipType;
  techLevel: TechLevel;
  resourceRating: ResourceRating;
  leadershipRating: LeadershipRating;
  leaderId?: string;
}
