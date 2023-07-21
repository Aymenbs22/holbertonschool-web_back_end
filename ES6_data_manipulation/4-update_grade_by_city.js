export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  if (!Array.isArray(getListStudents)) {
    return [];
  }
  if (!Array.isArray(city)) {
    return [];
  }
  if (!Array.isArray(newGrades)) {
    return [];
  }
  const i = 0;
  const sumWithInitial = getListStudents.reduce(
    (accumulator, currentValue) => accumulator + currentValue.id, i,
  );
  return sumWithInitial;
}
