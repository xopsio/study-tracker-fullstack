
export async function getRoot() {
  try {
    const res = await fetch('/');
    return await res.json();
  } catch (e) {
    return { message: 'server not responding'};
  }
}