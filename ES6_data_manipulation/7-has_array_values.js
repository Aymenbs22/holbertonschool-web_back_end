export default function hasValuesFromArray(set, array) {
  const bool = array.every((element) => set.has(element));
  return bool;
}
