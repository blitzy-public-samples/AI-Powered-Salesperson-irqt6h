import React from 'react';
import { UserManagement } from './UserManagement';
import { SystemConfig } from './SystemConfig';
import { Analytics } from './Analytics';

const AdminDashboard: React.FC = () => {
  return (
    <div className="admin-dashboard">
      <h1>Admin Dashboard</h1>
      <div className="dashboard-content">
        <UserManagement />
        <SystemConfig />
        <Analytics />
      </div>
    </div>
  );
};

export default AdminDashboard;