const fs = require('fs').promises;

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, { encoding: 'utf8' });
    console.log(data);
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}
module.exports = countStudents;
