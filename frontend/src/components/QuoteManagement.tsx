import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { selectQuotes, generateQuote } from '../store/quoteSlice';
import QuoteList from './QuoteList';
import QuoteDetails from './QuoteDetails';

const QuoteManagement: React.FC = () => {
  const dispatch = useDispatch();
  const quotes = useSelector(selectQuotes);
  const [selectedQuote, setSelectedQuote] = useState<string | null>(null);

  const handleQuoteSelection = (quoteId: string) => {
    setSelectedQuote(quoteId);
  };

  const handleGenerateQuote = () => {
    dispatch(generateQuote());
  };

  return (
    <div className="quote-management">
      <h1>Quote Management</h1>
      <div className="quote-container">
        <QuoteList 
          quotes={quotes} 
          onSelectQuote={handleQuoteSelection}
        />
        {selectedQuote && (
          <QuoteDetails 
            quote={quotes.find(q => q.id === selectedQuote)} 
          />
        )}
      </div>
      <button onClick={handleGenerateQuote}>Generate New Quote</button>
    </div>
  );
};

export default QuoteManagement;