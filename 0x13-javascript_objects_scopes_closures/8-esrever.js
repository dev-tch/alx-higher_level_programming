#!/usr/bin/node
function addItem (newArray, current) {
  newArray.push(current);
  return newArray;
}
exports.esrever = function (list) {
  return list.reduceRight(addItem, []);
};
