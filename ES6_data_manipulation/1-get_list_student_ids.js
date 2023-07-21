export default function getListStudentIds(StudentIds) {
  if (!Array.isArray(StudentIds)) {
    return [];
  }
  const StudentIdss = StudentIds.map((StudentIds) => StudentIds.id);
  return StudentIdss;
}
