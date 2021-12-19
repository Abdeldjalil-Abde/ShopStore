// opening the filter mene //
const filterMene = document.querySelector(".filter-mene");
const filterMeneBtn = document.querySelector(".filter-mene .open");

const filterPar = document.querySelector(".filter-par");
const toolsPar = document.querySelector(".tools-par");
const market = document.querySelector(".market");

filterMene.addEventListener("click", (e) => {
    filterMene.classList.toggle("active");
    filterPar.classList.toggle("mene-opened");
    toolsPar.classList.toggle("mene-opened");
    market.classList.toggle("mene-opened");
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
        itemsPointer--;
        filter.style.left =
            -itemsPointer * (filtersFrameworkWidth / filtersAppearNum) + "px";
    }
});

filterRightBtn.addEventListener("click", (e) => {
    if (itemsPointer < filterItems.length - filtersAppearNum) {
        itemsPointer++;
        filter.style.left =
            -itemsPointer * (filtersFrameworkWidth / filtersAppearNum) + "px";
    }
});

//  //

// URL //
function getUrlParameters() {
    let urlStr = window.location.search.split("?")[1].split("&");

    let urlPar = [];
    urlStr.forEach((obj) => {
        let name = obj.split("=")[0];
        let value = obj.split("=")[1];
        value = value.replaceAll("%22", "");
        value = value.replaceAll("%27", "");
        value = value.replaceAll("%20", " ");

        urlPar.push({ name, value });
    });

    return urlPar;
}

const filterMeneContainer = document.querySelector(".filter-mene .container");

function setFilterMene(type) {
    let typesItems = {
        clothes: [
            { name: "shirts",   logo: "../img/icon/clothe/shirt.png" },
            { name: "pants",    logo: "../img/icon/clothe/pant.png" },
            { name: "shoes",    logo: "../img/icon/clothe/shoes.png" },
            { name: "coats",    logo: "../img/icon/clothe/coat.png" },
            { name: "hats",     logo: "../img/icon/clothe/hat.png" },
            { name: "dresses",  logo: "../img/icon/clothe/dress.png" },
            { name: "skirts",   logo: "../img/icon/clothe/skirt.png" },
            { name: "more",     logo: "../img/icon/more.png" },
        ],
    };

    let items = "";

    typesItems[type].forEach((obj) => {
        items +=
            '<a href="" class="item"><img src="' +
            obj["logo"] +
            '" alt="" class="logo" /><p class="content">' +
            obj["name"] +
            "</p></a>";
    });

    filterMeneContainer.innerHTML = items;
}

const filterItemsLink = document.querySelectorAll(
    ".filter-par .filters .types li a"
);

let urlPar = getUrlParameters();
urlPar.forEach((obj) => {
    switch (obj["name"]) {
        case "product_type":
            {
                filterItemsLink.forEach((filter) => {
                    if (obj["value"] == filter.innerText.toLowerCase()) {
                        filter.classList.add("active");
                    }
                });

                setFilterMene(obj["value"]);
            }

            break;

        default:
            break;
    }
});
//  //
