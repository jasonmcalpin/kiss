export interface apiResponse<T> {
  success: boolean;
  message?: string;
  data?: T;
}
export interface apiError {
  success: false;
  message: string;
}
export interface apiSuccess<T> {
  success: true;
  data: T;
}
export interface apiRequest<T> {
  method: string;
  endpoint: string;
  body?: T;
}
