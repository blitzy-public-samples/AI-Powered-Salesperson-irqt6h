import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { User } from '../schema/user';

interface UserState {
  currentUser: User | null;
  isAuthenticated: boolean;
  error: string | null;
}

const initialState: UserState = {
  currentUser: null,
  isAuthenticated: false,
  error: null,
};

const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    setCurrentUser: (state, action: PayloadAction<User | null>) => {
      state.currentUser = action.payload;
      state.isAuthenticated = action.payload !== null;
      state.error = null;
    },
    updateAuthStatus: (state, action: PayloadAction<boolean>) => {
      state.isAuthenticated = action.payload;
    },
    setError: (state, action: PayloadAction<string>) => {
      state.error = action.payload;
    },
    clearError: (state) => {
      state.error = null;
    },
  },
});

export const { setCurrentUser, updateAuthStatus, setError, clearError } = userSlice.actions;
export default userSlice.reducer;