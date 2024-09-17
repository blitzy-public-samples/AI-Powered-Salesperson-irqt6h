import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { Provider } from 'react-redux';
import { store } from './store';
import { ChatInterface } from './components/ChatInterface';
import { QuoteManagement } from './components/QuoteManagement';
import { AdminDashboard } from './components/AdminDashboard';
import { UserAuthentication } from './components/UserAuthentication';
import { Home } from './pages/Home';
import { Chat } from './pages/Chat';
import { Quotes } from './pages/Quotes';
import { Admin } from './pages/Admin';
import { Profile } from './pages/Profile';

const App: React.FC = () => {
  return (
    <Provider store={store}>
      <BrowserRouter>
        <UserAuthentication>
          <Switch>
            <Route exact path="/" component={Home} />
            <Route path="/chat" component={Chat} />
            <Route path="/quotes" component={Quotes} />
            <Route path="/admin" component={Admin} />
            <Route path="/profile" component={Profile} />
          </Switch>
        </UserAuthentication>
      </BrowserRouter>
    </Provider>
  );
};

export default App;

// HUMAN ASSISTANCE NEEDED
// The following improvements might be necessary for production readiness:
// 1. Implement proper authentication checks for protected routes (e.g., /admin, /profile)
// 2. Add error boundaries to catch and handle runtime errors
// 3. Implement lazy loading for route components to improve initial load time
// 4. Add a 404 Not Found route for unmatched paths
// 5. Consider adding a layout component to wrap all routes for consistent UI elements (e.g., header, footer)