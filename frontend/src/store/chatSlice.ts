import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { ChatSession, Message } from '../schema/chat';

interface ChatState {
  sessions: ChatSession[];
  currentSession: ChatSession | null;
  error: string | null;
}

const initialState: ChatState = {
  sessions: [],
  currentSession: null,
  error: null,
};

const chatSlice = createSlice({
  name: 'chat',
  initialState,
  reducers: {
    startSession: (state) => {
      const newSession: ChatSession = {
        id: Date.now().toString(),
        messages: [],
        startTime: new Date().toISOString(),
        endTime: null,
      };
      state.sessions.push(newSession);
      state.currentSession = newSession;
      state.error = null;
    },
    endSession: (state) => {
      if (state.currentSession) {
        state.currentSession.endTime = new Date().toISOString();
        state.currentSession = null;
      }
    },
    addMessage: (state, action: PayloadAction<Message>) => {
      if (state.currentSession) {
        state.currentSession.messages.push(action.payload);
      } else {
        state.error = 'No active session to add message to';
      }
    },
    setError: (state, action: PayloadAction<string>) => {
      state.error = action.payload;
    },
    clearError: (state) => {
      state.error = null;
    },
  },
});

export const { startSession, endSession, addMessage, setError, clearError } = chatSlice.actions;
export default chatSlice.reducer;