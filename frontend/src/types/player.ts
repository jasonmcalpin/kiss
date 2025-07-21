export interface Player {
  id: string;
  name: string;
  empireId: string;
  flagUrl?: string;
  color?: string;
  resources: number;
  techLevel: number;
  leadershipRating: number;
  leaderList: string[];
}