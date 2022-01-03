// action button //
const visitForm = document.querySelector("section.visit");
const editForm = document.querySelector("section.edit");

const editBtn = document.querySelector("section.visit .action .edit");
const contactBtn = document.querySelector("section.visit .action .contact");

if (urlPar["profile_action"] == "owner visit") {
    editBtn.classList.add("show");
} else if (urlPar["profile_action"] == "user visit") {
    contactBtn.classList.add("show");
} else if (urlPar["profile_action"] == "edit") {
    visitForm.classList.add("hide");
    editForm.classList.add("show");
}
//  //

// profile img //
const img_input = document.querySelector(".edit .avatar .img input");
const profileImg = document.querySelector(".edit .avatar .img img");

main_img_input.addEventListener("change", () => {
    const reader = new FileReader();

    reader.addEventListener("load", () => {
        mainImg.setAttribute("src", reader.result);
    });

    reader.readAsDataURL(main_img_input.files[0]);
});
//  //
