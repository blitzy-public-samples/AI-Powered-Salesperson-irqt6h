import { login } from 'app/services/api';
import { AppDispatch, setUser, clearUser } from 'app/store';

export const authenticateUser = async (email: string, password: string, dispatch: AppDispatch): Promise<void> => {
  try {
    const response = await login(email, password);
    const { token, user } = response.data;
    
    // Store JWT token in localStorage
    localStorage.setItem('authToken', token);
    
    // Dispatch setUser action to update Redux store
    dispatch(setUser(user));
  } catch (error) {
    // HUMAN ASSISTANCE NEEDED
    // Error handling should be implemented here. Consider:
    // - Displaying error messages to the user
    // - Logging errors for debugging purposes
    // - Handling different types of errors (network, authentication, etc.)
    console.error('Authentication failed:', error);
    throw error;
  }
};

export const logoutUser = (dispatch: AppDispatch): void => {
  // Remove JWT token from localStorage
  localStorage.removeItem('authToken');
  
  // Dispatch clearUser action to update Redux store
  dispatch(clearUser());
};