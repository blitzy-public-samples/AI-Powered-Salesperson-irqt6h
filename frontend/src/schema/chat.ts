import { createSlice, PayloadAction } from '@reduxjs/toolkit';

// Interfaces
interface Message {
  id: string;
  content: string;
  sender: string;
  timestamp: Date;
}

interface ChatSession {
  id: string;
  userId: string;
  messages: Message[];
  startTime: Date;
  endTime: Date;
  status: string;
}

interface ChatState {
  sessions: ChatSession[];
  currentSessionId: string;
  isLoading: boolean;
  error: string;
}

// HUMAN ASSISTANCE NEEDED
// The following chatSlice implementation may need review and adjustments for production readiness
const initialState: ChatState = {
  sessions: [],
  currentSessionId: '',
  isLoading: false,
  error: '',
};

const chatSlice = createSlice({
  name: 'chat',
  initialState,
  reducers: {
    addMessage: (state, action: PayloadAction<{ sessionId: string; message: Message }>) => {
      const session = state.sessions.find(s => s.id === action.payload.sessionId);
      if (session) {
        session.messages.push(action.payload.message);
      }
    },
    startSession: (state, action: PayloadAction<ChatSession>) => {
      state.sessions.push(action.payload);
      state.currentSessionId = action.payload.id;
    },
    endSession: (state, action: PayloadAction<string>) => {
      const session = state.sessions.find(s => s.id === action.payload);
      if (session) {
        session.endTime = new Date();
        session.status = 'ended';
      }
    },
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.isLoading = action.payload;
    },
    setError: (state, action: PayloadAction<string>) => {
      state.error = action.payload;
    },
  },
});

export const { addMessage, startSession, endSession, setLoading, setError } = chatSlice.actions;
export default chatSlice.reducer;