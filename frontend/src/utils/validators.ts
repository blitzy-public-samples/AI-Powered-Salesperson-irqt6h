// frontend/src/utils/validators.ts

export const isValidEmail = (email: string): boolean => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

// HUMAN ASSISTANCE NEEDED
// The following function has a confidence level below 0.8 and may need review
export const isValidPassword = (password: string): boolean => {
  // Check password length (at least 8 characters)
  if (password.length < 8) return false;

  // Check for presence of uppercase and lowercase letters
  if (!/[a-z]/.test(password) || !/[A-Z]/.test(password)) return false;

  // Check for presence of numbers
  if (!/\d/.test(password)) return false;

  // Check for presence of special characters
  if (!/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password)) return false;

  return true;
};

export const isValidSKU = (sku: string): boolean => {
  const skuRegex = /^[A-Z]{3}-\d{3}-[A-Z]\d{2}$/;
  return skuRegex.test(sku);
};