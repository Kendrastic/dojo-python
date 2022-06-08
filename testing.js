function bubbleSort(toSort) {
  for (let j = 0; j < toSort.length; j++) {
    for (var i = 0; i < toSort.length - 1; i++) {
      var currentVal = toSort[i];
      var nextVal = toSort[i + 1];

      if (currentVal > nextVal) {
        toSort[i + 1] = currentVal;
        toSort[i] = nextVal;
      }
    }
  }
  return toSort;
}

// loop over each of the array elements
// compare current index value against next index value
// if current value is greater than next, swap index
// loop as many elements as

function range(size, startAt = 0) {
  return [...Array(size).keys()]
    .map((i) => i + startAt)
    .sort(() => 0.5 - Math.random());
}
console.log(bubbleSort(range(10)));
