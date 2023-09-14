/* eslint-disable */
export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const task = true; // Block-scoped variable, does not affect outer task
    const task2 = false; // Block-scoped variable, does not affect outer task2
  }

  return [task, task2];
}
