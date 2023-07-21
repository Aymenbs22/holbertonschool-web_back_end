export const weakMap = new WeakMap();
export default function queryAPI(endpoint) {
  if (!weakMap && !endpoint) {
    throw new Error('Endpoint load is high');
  }
}
