export default function getStudentsByLocation(StudentIds, city) {
  if (!Array.isArray(StudentIds)) {
    return [];
  }
  const StudentIdss = StudentIds.filter((StudentIds) => StudentIds.location === city);
  return StudentIdss;
}
