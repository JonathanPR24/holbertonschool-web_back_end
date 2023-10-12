function cleanSet(set, startString) {
  const filteredValues = new Set();

  for (const value of set) {
    if (value.startsWith(startString)) {
      const restOfValue = value.slice(startString.length);
      filteredValues.add(restOfValue);
    }
  }

  return Array.from(filteredValues).join('-');
}

export default cleanSet;
