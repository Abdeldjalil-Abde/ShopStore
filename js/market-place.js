// opening the filter mene //
const filterMene = document.querySelector(".filter-mene");
const filterMeneBtn = document.querySelector(".filter-mene .open");

filterMene.addEventListener("click", (e) => {
    filterMene.classList.toggle("active");
});

//  //

// filter par style //
const filterLeftBtn = document.querySelector(".filter-par .left button");
const filterRightBtn = document.querySelector(".filter-par .right button");

const filterFramework = document.querySelector(".filter-par .filters");
const filter = document.querySelector(".filter-par .filters .types");
const filterItems = document.querySelectorAll(".filter-par .filters .types li");

const filtersFrameworkStyle = window.getComputedStyle(filterFramework);
const filterStyle = window.getComputedStyle(filter);

let filtersFrameworkWidth = filtersFrameworkStyle
    .getPropertyValue("width")
    .split("px")[0];

filterItems.forEach((obj) => {
    obj.style.width = filtersFrameworkWidth / 3 + "px";
});

let itemsPointer = 0;

filterLeftBtn.addEventListener("click", (e) => {
    if (itemsPointer > 0) {
        itemsPointer--;
        filter.style.left = -itemsPointer * (filtersFrameworkWidth / 3) + "px";
    }
});

filterRightBtn.addEventListener("click", (e) => {
    if (itemsPointer < filterItems.length - 3) {
        itemsPointer++;
        filter.style.left = -itemsPointer * (filtersFrameworkWidth / 3) + "px";
    }
});

//  //
