import React from 'react';
import { UserManagement, SystemConfig, Analytics } from '../components/AdminDashboard';
import { useAuth } from '../services/auth';
import { Navigate } from 'react-router-dom';

// HUMAN ASSISTANCE NEEDED
// The following component needs review for production readiness.
// Additional error handling, loading states, and styling may be required.
// The authentication and authorization logic might need to be more robust.

const Admin: React.FC = () => {
  const { user, isAuthenticated, isAdmin } = useAuth();

  if (!isAuthenticated || !isAdmin) {
    return <Navigate to="/login" replace />;
  }

  return (
    <div className="admin-dashboard">
      <h1>Admin Dashboard</h1>
      <div className="admin-sections">
        <UserManagement />
        <SystemConfig />
        <Analytics />
      </div>
    </div>
  );
};

export default Admin;