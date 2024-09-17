import { configureStore } from '@reduxjs/toolkit';
import { chatReducer } from './chatSlice';
import { quoteReducer } from './quoteSlice';
import { userReducer } from './userSlice';

const store = configureStore({
  reducer: {
    chat: chatReducer,
    quote: quoteReducer,
    user: userReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export default store;