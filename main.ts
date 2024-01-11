const fs = require('fs');

function readFileContent(fileName) {
  const filePath = fileName; // Potentially vulnerable code
  const content = fs.readFileSync(filePath, 'utf-8');
  return content;
}

// Simulating user input (replace this with your actual user input)
const userInput = prompt("Please enter file name");;

// Potentially vulnerable code: using user input in a filesystem operation
const fileContent = readFileContent(userInput);
console.log(fileContent);
