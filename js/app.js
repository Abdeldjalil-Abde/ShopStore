let header = document.querySelector(".top-par");

window.addEventListener("scroll", (e) => {
    if (window.scrollY > 200) {
        header.classList.add("scrolled");
    } else {
        header.classList.remove("scrolled");
    }
});
