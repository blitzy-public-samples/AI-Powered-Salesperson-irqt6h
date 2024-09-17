import axios, { AxiosInstance } from 'axios';
import { RootState } from 'app/store';
import { ChatSession, Message } from 'app/schema/chat';
import { Quote } from 'app/schema/quote';
import { User } from 'app/schema/user';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

const createApiInstance = (): AxiosInstance => {
  const instance = axios.create({
    baseURL: API_BASE_URL,
  });

  instance.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  });

  instance.interceptors.response.use(
    (response) => response,
    (error) => {
      if (error.response && error.response.status === 401) {
        // Handle unauthorized access (e.g., redirect to login)
      }
      return Promise.reject(error);
    }
  );

  return instance;
};

export const login = async (email: string, password: string): Promise<string> => {
  const api = createApiInstance();
  const response = await api.post('/auth/login', { email, password });
  return response.data.token;
};

export const getChatSessions = async (): Promise<ChatSession[]> => {
  const api = createApiInstance();
  const response = await api.get('/chat/sessions');
  return response.data;
};

export const sendMessage = async (sessionId: string, content: string): Promise<Message> => {
  const api = createApiInstance();
  const response = await api.post(`/chat/sessions/${sessionId}/messages`, { content });
  return response.data;
};

// HUMAN ASSISTANCE NEEDED
// The generateQuote function might need additional error handling or validation
export const generateQuote = async (sessionId: string): Promise<Quote> => {
  const api = createApiInstance();
  const response = await api.post('/quotes', { sessionId });
  return response.data;
};