#!/usr/bin/node
const request = require('request');
const apiTask = process.argv[2];
const stats = { };
let doneTasks;
function test (completed) {
  if (completed) {
    return 1;
  } else {
    return 0;
  }
}
request(apiTask, (error, response, body) => {
  if (error) {
    console.error('Error: ', error);
  } else {
    const jsonObject = JSON.parse(body);
    jsonObject.forEach(function (itemJson) {
      const id = itemJson.userId;
      if (!Object.hasOwnProperty.call(stats, id)) {
        doneTasks = test(jsonObject.completed);
        stats[id] = doneTasks;
      } else {
        doneTasks = Number(stats[id]);
        doneTasks = doneTasks + test(itemJson.completed);
        stats[id] = doneTasks;
      }
    });
    console.log(stats);
  }
});
