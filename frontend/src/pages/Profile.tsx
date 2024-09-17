import React, { useState } from 'react';
import { useAuth } from '../services/auth';
import { updateUserProfile } from '../services/api';
import { ProfileForm } from '../components/UserAuthentication';

const Profile: React.FC = () => {
  const { user, setUser } = useAuth();
  const [message, setMessage] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleProfileUpdate = async (updatedData: any) => {
    setIsLoading(true);
    setMessage(null);

    try {
      const updatedUser = await updateUserProfile(updatedData);
      setUser(updatedUser);
      setMessage('Profile updated successfully');
    } catch (error) {
      setMessage('Failed to update profile. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  if (!user) {
    return <div>Please log in to view your profile.</div>;
  }

  return (
    <div className="profile-page">
      <h1>User Profile</h1>
      {message && <div className={message.includes('Failed') ? 'error' : 'success'}>{message}</div>}
      <ProfileForm
        initialData={user}
        onSubmit={handleProfileUpdate}
        isLoading={isLoading}
      />
    </div>
  );
};

export default Profile;