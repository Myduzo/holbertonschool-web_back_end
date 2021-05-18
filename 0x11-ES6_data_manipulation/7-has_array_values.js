export default function hasValuesFromArray(set, array) {
  return array.filter((x) => set.has(x)).length === array.length;
}
