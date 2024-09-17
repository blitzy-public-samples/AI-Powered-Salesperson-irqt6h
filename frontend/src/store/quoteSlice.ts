import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { Quote } from '../schema/quote';

interface QuoteState {
  quotes: Quote[];
  currentQuote: Quote | null;
  error: string | null;
}

const initialState: QuoteState = {
  quotes: [],
  currentQuote: null,
  error: null,
};

const quoteSlice = createSlice({
  name: 'quote',
  initialState,
  reducers: {
    addQuote: (state, action: PayloadAction<Quote>) => {
      state.quotes.push(action.payload);
    },
    updateQuote: (state, action: PayloadAction<Quote>) => {
      const index = state.quotes.findIndex(quote => quote.id === action.payload.id);
      if (index !== -1) {
        state.quotes[index] = action.payload;
      }
    },
    setCurrentQuote: (state, action: PayloadAction<Quote>) => {
      state.currentQuote = action.payload;
    },
    clearCurrentQuote: (state) => {
      state.currentQuote = null;
    },
    setError: (state, action: PayloadAction<string>) => {
      state.error = action.payload;
    },
    clearError: (state) => {
      state.error = null;
    },
  },
});

export const { 
  addQuote, 
  updateQuote, 
  setCurrentQuote, 
  clearCurrentQuote, 
  setError, 
  clearError 
} = quoteSlice.actions;

export default quoteSlice.reducer;