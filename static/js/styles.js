// document.getElementById("star").addEventListener('click', function (click) {
//     document.getElementById("star").classList.toggle("unchecked")
//     document.getElementById("star").classList.add("checked")
// })

// #dynamic star rating reviews
var list = ['one', 'two', 'three', 'four', 'five'];
list.forEach(function (element) {
    document.getElementById(element).addEventListener("click", function () {
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

var rating_count;
var list = ['one', 'two', 'three', 'four', 'five'];
list.forEach(function (element) {
    rating_count = [0];
    var clicked = document.getElementById(element).addEventListener("click", function () {

        var cln = document.getElementById(element).className;
        if (cln.includes("checked")) {
            rating_count++
            document.getElementById('out-of').textContent = rating_count
        }

        else if (clicked) {
            rating_count--
            document.getElementById('out-of').textContent = rating_count
        }


    })

})

var rating_count;
var list = ['one', 'two', 'three', 'four', 'five'];
list.forEach(function (element) {
    rating_count = [0];
    document.getElementById(element).addEventListener("click", function () {

        var cln = document.getElementById(element).className;
        if (cln.includes("unchecked")) {
            rating_count--
            document.querySelector('#out-of').textContent = rating_count
        }

        else {
            rating_count + 1
            document.querySelector('#out-of').textContent = rating_count
        }

        rating_count= request.form.get("rating")

    })

})

