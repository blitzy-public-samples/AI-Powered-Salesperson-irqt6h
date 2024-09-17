import React from 'react';
import { Link } from 'react-router-dom';
import { ChatInterface } from '../components/ChatInterface';
import { useAuth } from '../services/auth';

const Home: React.FC = () => {
  const { isAuthenticated } = useAuth();

  return (
    <div className="home-container">
      <h1>Welcome to AI-powered Salesperson Chat</h1>
      <p>Get instant assistance and boost your sales with our AI chatbot.</p>
      
      {isAuthenticated ? (
        <div>
          <p>Ready to chat? Start a new conversation now!</p>
          <ChatInterface />
        </div>
      ) : (
        <div>
          <p>Please log in to start chatting with our AI salesperson.</p>
          <Link to="/login" className="cta-button">
            Log In
          </Link>
        </div>
      )}
      
      <div className="quick-links">
        <h2>Quick Links</h2>
        <ul>
          <li><Link to="/features">Explore Features</Link></li>
          <li><Link to="/pricing">View Pricing</Link></li>
          <li><Link to="/about">About Us</Link></li>
        </ul>
      </div>
    </div>
  );
};

export default Home;