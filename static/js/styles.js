// document.getElementById("star").addEventListener('click', function (click) {
//     document.getElementById("star").classList.toggle("unchecked")
//     document.getElementById("star").classList.add("checked")
// })

// #dynamic star rating reviews
var list = ['one', 'two', 'three', 'four', 'five'];
list.forEach(function (element) {
    document.getElementById(element).addEventListener("click", function (list) {
        var cls = document.getElementById(element).className;
        if (cls.includes("unchecked")) {
            document.getElementById(element).classList.remove("unchecked");
            document.getElementById(element).classList.add("checked");
        }
        else {
            document.getElementById(element).classList.remove("checked"); document.getElementById(element).classList.add("unchecked");
        }
    });
});

document.getElementById("submit").addEventListener('click', function () {
    document.getElementById("submit").classList.toggle("clicked")
})

var list = ['one', 'two', 'three', 'four', 'five'];
list.forEach(function (element) {
    var rating_count = 0;
    document.getElementById(element).addEventListener("click", function () {
        rating_count++
        document.querySelector('#out-of').textContent = rating_count

    })

})

