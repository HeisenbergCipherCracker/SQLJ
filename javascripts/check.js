function checkInputForSQLInjection(input) {
  // Define a regular expression pattern to check for SQL keywords or suspicious characters
  const sqlPattern = /(\b(ALTER|CREATE|DELETE|DROP|EXEC(UTE){0,1}|INSERT( +INTO){0,1}|MERGE|SELECT|UPDATE|UNION( +ALL){0,1})\b)|(--)|(;)|(')/gi;

  // Check if the input matches the SQL pattern
  if (sqlPattern.test(input)) {
    console.log('Potential SQL injection detected!');
    return false;
  }

  // Input is considered safe
  return true;
}

// Get the URL input from the user
const userInput = prompt('Enter the URL:'); // For browser environment

// For Node.js environment, use:
// const userInput = process.argv[2];

// Check input for SQL injection
const isSafe = checkInputForSQLInjection(userInput);
console.log(isSafe); // Output: Potential SQL injection detected! false