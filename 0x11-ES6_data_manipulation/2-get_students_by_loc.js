export default function getStudentsByLocation(getListStudents, city) {
  return getListStudents.filter((idx) => idx.location.localeCompare(city) === 0);
}
