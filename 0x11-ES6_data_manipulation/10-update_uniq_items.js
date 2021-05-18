export default function updateUniqueItems(items) {
  if (!(items instanceof Map)) throw (Error('Cannot process'));
  items.forEach((x, y) => {
    if (x === 1) items.set(y, 100);
  });
  return items;
}
