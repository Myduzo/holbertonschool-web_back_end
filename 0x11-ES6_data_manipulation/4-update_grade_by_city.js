export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  const result = getListStudents.filter((student) => student.location.localeCompare(city) === 0);
  result.map((data) => {
    const newGrade = newGrades.filter((x) => x.studentId === data.id);
    const student = data;
    if (newGrade.length === 1) student.grade = newGrade[0].grade;
    else student.grade = 'N/A';
    return student;
  });
  return result;
}
