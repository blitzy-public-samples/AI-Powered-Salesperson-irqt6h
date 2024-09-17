import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { ChatInterface } from '../components/ChatInterface';
import { selectCurrentSession, startNewSession } from '../store/chatSlice';
import { sendMessage } from '../services/api';

// HUMAN ASSISTANCE NEEDED
// This component may need additional error handling and optimization for production readiness.
// Please review and enhance as necessary.

const Chat: React.FC = () => {
  const dispatch = useDispatch();
  const currentSession = useSelector(selectCurrentSession);
  const [messages, setMessages] = useState<Array<{ role: string; content: string }>>([]);

  useEffect(() => {
    if (!currentSession) {
      dispatch(startNewSession());
    }
  }, [dispatch, currentSession]);

  const handleSendMessage = async (message: string) => {
    setMessages(prevMessages => [...prevMessages, { role: 'user', content: message }]);
    
    try {
      const response = await sendMessage(currentSession?.id || '', message);
      setMessages(prevMessages => [...prevMessages, { role: 'assistant', content: response }]);
    } catch (error) {
      console.error('Error sending message:', error);
      // TODO: Implement proper error handling and user feedback
    }
  };

  const handleNewSession = () => {
    dispatch(startNewSession());
    setMessages([]);
  };

  return (
    <ChatInterface
      messages={messages}
      onSendMessage={handleSendMessage}
      onNewSession={handleNewSession}
    />
  );
};

export default Chat;