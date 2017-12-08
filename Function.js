function unDouble(arr,string){
  var allValues = [];
  var dd = false
  for (var i=0; i<arr.length; i++) {
  var splitLen = arr[i].split(' ');
  if (splitLen.length > 2)
      {
          key = new RegExp('(.*)' + string + '(.*)', "g");
          if (key.test(arr[i]) == false) {
  			  allValues.push(arr[i]);
          }
          else if (dd == false) {
          allValues.push(arr[i]);
          dd = true
          }
      }

  }
return allValues
}

//  console.log(key);
//  console.log(allValues);
