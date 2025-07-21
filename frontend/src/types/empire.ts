export interface Empire {
  id: string;
  name: string;
  leaderId: string;
  color?: string;
  resources: number;
  techLevel: number;
  sectors: string[];
}