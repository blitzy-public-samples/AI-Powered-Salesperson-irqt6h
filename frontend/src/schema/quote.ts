import { createSlice, PayloadAction } from '@reduxjs/toolkit';

// Interfaces
export interface QuoteItem {
  id: string;
  skuId: string;
  quantity: number;
  unitPrice: number;
  totalPrice: number;
}

export interface Quote {
  id: string;
  userId: string;
  createdAt: Date;
  updatedAt: Date;
  status: string;
  totalAmount: number;
  items: QuoteItem[];
}

export interface QuoteState {
  quotes: Quote[];
  currentQuoteId: string;
  isLoading: boolean;
  error: string;
}

// HUMAN ASSISTANCE NEEDED
// The following quoteSlice implementation may need review and adjustments for production readiness
export const quoteSlice = createSlice({
  name: 'quote',
  initialState: {
    quotes: [],
    currentQuoteId: '',
    isLoading: false,
    error: '',
  } as QuoteState,
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
    setCurrentQuote: (state, action: PayloadAction<string>) => {
      state.currentQuoteId = action.payload;
    },
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.isLoading = action.payload;
    },
    setError: (state, action: PayloadAction<string>) => {
      state.error = action.payload;
    },
  },
});

export const { addQuote, updateQuote, setCurrentQuote, setLoading, setError } = quoteSlice.actions;

export default quoteSlice.reducer;