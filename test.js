// let nums = [11, 27, 39, [2, 4], 50];

// function mapped(arr) {
//   let out = [];

//   // arr.forEach(n => {
//   //   if (typeof n == "object") {
//   //     console.log("fount a nested array", n);
//   //   } else {
//   //     out.push(n * 2);
//   //   }
//   // });

//   for (let i = 0; i < arr.length; i++) {
//     if (typeof arr[i] == "object") {
//       console.log("found a nested array", arr[i]);
//       out.push(arr[i]);
//     } else {
//       out.push(arr[i] * 2);
//     }
//   }

//   return out;
// }
// console.log(mapped(nums));

// let nums = [11, 27, 39, [2, 4], 50];

// for (let i = 0; i < nums.length; i++) {
//   if (typeof nums[i] == "object") {
//     console.log("found a nested array", nums[i]);
//   }
//   else {
//     nums[i] * 2;
//   }
// }

// console.log(nums);

// let txt = 'but soft what light in yonder window breaks';
// let words = txt.split(" ");

// let words_arr = [];

// words.forEach(word => {
//   words_arr.push([word.length ,word]);
// });

// words_arr.sort((a, b) => b[0] - a[0]);

// words_arr.forEach(w => {
//   w.shift();
// });

// let new_arr = words_arr.flat()

// console.log(new_arr);

