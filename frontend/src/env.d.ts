export {};

declare global {
  interface Window {
    _env_: {
      VITE_API_URL: string;
      VITE_CORS_ORIGINS?: string;
    };
  }
}
