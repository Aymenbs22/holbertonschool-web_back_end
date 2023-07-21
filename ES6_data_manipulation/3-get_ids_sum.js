export default function getStudentIdsSum(getListStudents) {
  if (!Array.isArray(getListStudents)) {
    return [];
  }
  const i = 0;
  const sumWithInitial = getListStudents.reduce(
    (accumulator, currentValue) => accumulator + currentValue.id, i,
  );
  return sumWithInitial;
}
