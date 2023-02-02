#!/usr/bin/node

exports.esrever = function (list) {
  let j = list.length - 1;
  const revList = [];
  for (let i = 0; i < list.length; i++) {
    revList[j] = list[i];
    j--;
  }
  return (revList);
};
