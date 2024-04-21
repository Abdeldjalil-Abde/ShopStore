const filterPar = document.querySelector(".filter-par");
const toolsPar = document.querySelector(".tools-par");

// filter par style //
const filterLeftBtn = document.querySelector(".filter-par .left");//*************
const filterRightBtn = document.querySelector(".filter-par .right");//**********************

const filterFramework = document.querySelector(".filter-par .filters");
const filter = document.querySelector(".filter-par .filters .types");

const filterItems = document.querySelectorAll(".filter-par .filters .types li");

const market = document.querySelector("section.market");

const ListItems = document.querySelectorAll(".market .items");

// //
filterItems.forEach(function (obj) {
    obj.addEventListener("click", function () {
        ListItems.forEach((Item) => {
            if (Item.getAttribute("type_a") == obj.getAttribute("type_a")) {
                Item.style.display = "flex";
                filterItems.forEach(function (obj) {
                    obj.querySelector('a').classList.remove("selected")
                });
                obj.querySelector('a').classList.add("selected")
            } else {
                Item.style.display = "none";
            }
        });
    });
});


// //
const filtersFrameworkStyle = window.getComputedStyle(filterFramework);
const filterStyle = window.getComputedStyle(filter);

let filtersAppearNum = 5;

let filtersFrameworkWidth = filtersFrameworkStyle
    .getPropertyValue("width")
    .split("px")[0];

filterItems.forEach((obj) => {
    obj.style.width = filtersFrameworkWidth / filtersAppearNum + "px";
});

let itemsPointer = 0;

filterLeftBtn.addEventListener("click", (e) => {
    if (itemsPointer > 0) {
        // move to left //
        itemsPointer--;
        filter.style.left =
            -itemsPointer * (filtersFrameworkWidth / filtersAppearNum) + "px";
        //  //

        // enable the right button //
        filterRightBtn.classList.remove("disable");
        //  //

        // disable the left button if hit the edge //
        if (!(itemsPointer > 0)) {
            filterLeftBtn.classList.add("disable");
        }
        //  //
    }
});

filterRightBtn.addEventListener("click", (e) => {
    if (itemsPointer < filterItems.length - filtersAppearNum) {
        // move to right //
        itemsPointer++;
        filter.style.left =
            -itemsPointer * (filtersFrameworkWidth / filtersAppearNum) + "px";
        //  //

        // enable the left button //
        filterLeftBtn.classList.remove("disable");
        //  //

        // disable the right button if hit the edge //
        if (!(itemsPointer < filterItems.length - filtersAppearNum)) {
            filterRightBtn.classList.add("disable");
        }
        //  //
    }
});
//  //
