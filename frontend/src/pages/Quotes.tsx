import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { QuoteList, QuoteDetails } from '../components/QuoteManagement';
import { selectQuotes, fetchQuotes } from '../store/quoteSlice';
import { generateQuote } from '../services/api';

// HUMAN ASSISTANCE NEEDED
// The following component may need additional error handling, loading states, and optimization for production readiness.
// Please review and enhance as necessary.

const Quotes: React.FC = () => {
  const dispatch = useDispatch();
  const quotes = useSelector(selectQuotes);
  const [selectedQuoteId, setSelectedQuoteId] = useState<string | null>(null);
  const [isGenerating, setIsGenerating] = useState(false);

  useEffect(() => {
    dispatch(fetchQuotes());
  }, [dispatch]);

  const handleQuoteSelection = (quoteId: string) => {
    setSelectedQuoteId(quoteId);
  };

  const handleGenerateQuote = async () => {
    setIsGenerating(true);
    try {
      await generateQuote();
      dispatch(fetchQuotes());
    } catch (error) {
      console.error('Failed to generate quote:', error);
      // TODO: Add proper error handling and user feedback
    } finally {
      setIsGenerating(false);
    }
  };

  return (
    <div className="quotes-page">
      <h1>Quotes Management</h1>
      <button onClick={handleGenerateQuote} disabled={isGenerating}>
        {isGenerating ? 'Generating...' : 'Generate New Quote'}
      </button>
      <div className="quotes-container">
        <QuoteList
          quotes={quotes}
          onSelectQuote={handleQuoteSelection}
          selectedQuoteId={selectedQuoteId}
        />
        {selectedQuoteId && (
          <QuoteDetails
            quoteId={selectedQuoteId}
            onClose={() => setSelectedQuoteId(null)}
          />
        )}
      </div>
    </div>
  );
};

export default Quotes;