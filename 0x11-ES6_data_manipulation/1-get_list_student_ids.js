export default function getListStudentIds(data) {
  if (Array.isArray(data)) return data.map((idx) => idx.id);
  return [];
}
