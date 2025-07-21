import { Sector } from '../../../types/index';

export interface UniverseCreationData {
  name: string;
  size: number;
  playerCount: number;
  map: Sector[]
}
export interface UniverseCreationResponse {
  success: boolean;
  message?: string;
  universeId?: string;
}

export function createUniverse (data: UniverseCreationData): Promise<UniverseCreationResponse> {
  // This function would typically make an API call to create a universe
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({
        success: true,
        universeId: '12345'
      });
    }, 1000);
  });
}