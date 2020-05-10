// document.getElementById("star").addEventListener('click', function (click) {
//     document.getElementById("star").classList.toggle("unchecked")
//     document.getElementById("star").classList.add("checked")
// })

// #dynamic star rating reviews
var list=['one','two','three','four','five'];
list.forEach(function(element) {
  document.getElementById(element).addEventListener("click", function(){
    var cls=document.getElementById(element).className;
    if(cls.includes("unchecked"))
       {
   document.getElementById(element).classList.remove("unchecked");
  document.getElementById(element).classList.add("checked");
      }
    else
      {
  document.getElementById(element).classList.remove("checked");     document.getElementById(element).classList.add("unchecked");
      }
});
});