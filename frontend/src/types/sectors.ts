import { ResourceRating, TechLevel, Fleet } from './index';


export interface System {
  id: string;
  resourceRating: ResourceRating;
  techLevel: TechLevel;
  ownerId?: string;
}

export interface Sector {
  x: number;
  y: number;
  system?: System;
  fleets: Fleet[];
}

