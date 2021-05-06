export default function appendToEachArrayValue(array, appendString) {
  let idx = 0;
  for (const value of array) {
    /* eslint-disable */
    array[idx] = appendString + value;
    /* eslint-enable */
    idx += 1;
  }

  return array;
}
