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
const filterMeneBtnContent = document.querySelector(
    ".filter-mene .open .content"
);

function setFilterMene(type) {
    let typesItems = {
        clothes: [
            { name: "none", logo: "../img/icon/none.png" },
            { name: "shirts", logo: "../img/icon/clothe/shirt.png" },
            { name: "pants", logo: "../img/icon/clothe/pant.png" },
            { name: "shoes", logo: "../img/icon/clothe/shoes.png" },
            { name: "coats", logo: "../img/icon/clothe/coat.png" },
            { name: "hats", logo: "../img/icon/clothe/hat.png" },
            { name: "dresses", logo: "../img/icon/clothe/dress.png" },
            { name: "skirts", logo: "../img/icon/clothe/skirt.png" },
            { name: "more", logo: "../img/icon/more.png" },
        ],
        tools: [
            { name: "none", logo: "../img/icon/none.png" },
            { name: "hammer", logo: "../img/icon/tool/hammer.png" },
            { name: "painting", logo: "../img/icon/tool/painting.png" },
            { name: "saw", logo: "../img/icon/tool/saw.png" },
            { name: "screw driver", logo: "../img/icon/tool/screw-driver.png" },
            { name: "shovel", logo: "../img/icon/tool/shovel.png" },
            { name: "wrench", logo: "../img/icon/tool/wrench.png" },
            { name: "more", logo: "../img/icon/more.png" },
        ],
        vehicles: [
            { name: "none", logo: "../img/icon/none.png" },
            { name: "car", logo: "../img/icon/vehicle/car.png" },
            { name: "motorcycle", logo: "../img/icon/vehicle/motorcycle.png" },
            { name: "bike", logo: "../img/icon/vehicle/bike.png" },
            { name: "more", logo: "../img/icon/more.png" },
        ],
        "car parts": [
            { name: "none", logo: "../img/icon/none.png" },
            {
                name: "car engine",
                logo: "../img/icon/car parts/car-engine.png",
            },
            { name: "car wheel", logo: "../img/icon/car parts/car-wheel.png" },
            {
                name: "car battery",
                logo: "../img/icon/car parts/car-battery.png",
            },
            { name: "car chair", logo: "../img/icon/car parts/car-chair.png" },
            {
                name: "steering wheel",
                logo: "../img/icon/car parts/steering-wheel.png",
            },
            {
                name: "spare parts",
                logo: "../img/icon/car parts/spare-parts.png",
            },
            {
                name: "car electrics",
                logo: "../img/icon/car parts/car-electrics.png",
            },
            {
                name: "car structure",
                logo: "../img/icon/car parts/car-structure.png",
            },
            { name: "more", logo: "../img/icon/more.png" },
        ],
        electrics: [
            { name: "none", logo: "../img/icon/none.png" },
            { name: "tv", logo: "../img/icon/electric/tv.png" },
            {
                name: "air-conditioner",
                logo: "../img/icon/electric/air-conditioner.png",
            },
            { name: "fridge", logo: "../img/icon/electric/fridge.png" },
            { name: "freezer", logo: "../img/icon/electric/freezer.png" },
            { name: "heater", logo: "../img/icon/electric/heater.png" },
            { name: "light", logo: "../img/icon/electric/light.png" },
            { name: "oven", logo: "../img/icon/electric/oven.png" },
            { name: "stove", logo: "../img/icon/electric/stove.png" },
            { name: "more", logo: "../img/icon/more.png" },
        ],
        furniture: [
            { name: "none", logo: "../img/icon/none.png" },
            { name: "bed", logo: "../img/icon/furniture/bed.png" },
            { name: "chair", logo: "../img/icon/furniture/chair.png" },
            { name: "closet", logo: "../img/icon/furniture/closet.png" },
            { name: "mattress", logo: "../img/icon/furniture/mattress.png" },
            { name: "pillow", logo: "../img/icon/furniture/pillow.png" },
            { name: "sofa", logo: "../img/icon/furniture/sofa.png" },
            { name: "table", logo: "../img/icon/furniture/table.png" },
            { name: "more", logo: "../img/icon/more.png" },
        ],
        building: [
            { name: "none", logo: "../img/icon/none.png" },
            { name: "cement", logo: "../img/icon/building/cement.png" },
            { name: "paint", logo: "../img/icon/building/paint.png" },
            { name: "electrical", logo: "../img/icon/building/electrical.png" },
            { name: "more", logo: "../img/icon/more.png" },
        ],
        books: [
            { name: "none", logo: "../img/icon/none.png" },
            { name: "student", logo: "../img/icon/book/student-book.png" },
            { name: "language", logo: "../img/icon/book/language-book.png" },
            { name: "novel", logo: "../img/icon/book/novel.png" },
            { name: "children", logo: "../img/icon/book/children-book.png" },
            { name: "religious", logo: "../img/icon/book/religious-book.png" },
            { name: "more", logo: "../img/icon/more.png" },
        ],
    };

    let items = "";

    typesItems[type].forEach((obj) => {
        let linkClass = "item";

        urlPar.forEach((par) => {
            if (par["name"] == "filter_type" && par["value"] == obj["name"]) {
                linkClass += " active";
            }
        });

        items +=
            '<a href="?product_type=' +
            type +
            "&filter_type=" +
            obj["name"] +
            '" class="' +
            linkClass +
            '"><img src="' +
            obj["logo"] +
            '" alt="" class="logo" /><p class="content">' +
            obj["name"] +
            "</p></a>";
    });

    filterMeneContainer.innerHTML = items;
    filterMeneBtnContent.innerHTML = type;
}

const filterItemsLink = document.querySelectorAll(
    ".filter-par .filters .types li a"
);

let urlPar = getUrlParameters();
urlPar.forEach((obj) => {
    switch (obj["name"]) {
        case "product_type":
            {
                let productTypeIndex = 0;

                // active the product type //
                filterItemsLink.forEach((filter, index) => {
                    if (obj["value"] == filter.innerText.toLowerCase()) {
                        filter.classList.add("active");
                        productTypeIndex = index; // get the product type index ///
                        return;
                    }
                });
                //  //

                // scroll the product type filter to the active type //
                if (productTypeIndex < filterItems.length - filtersAppearNum) {
                    itemsPointer = productTypeIndex;
                } else {
                    itemsPointer = filterItems.length - filtersAppearNum;
                }

                filter.style.left =
                    -itemsPointer * (filtersFrameworkWidth / filtersAppearNum) +
                    "px";
                //  //

                // set the side mene types //
                setFilterMene(obj["value"]);
                //  //
            }

            break;

        default:
            break;
    }
});
//  //
