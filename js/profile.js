const visitForm = document.querySelector("section.visit")
const editForm = document.querySelector("section.edit")

const editBtn = document.querySelector("section.visit .action .edit")
const contactBtn = document.querySelector("section.visit .action .contact")

if(urlPar["profile_action"]=="owner visit"){
    editBtn.classList.add("show");
}else if(urlPar["profile_action"]=="user visit"){
    contactBtn.classList.add("show");
}else if(urlPar["profile_action"]=="edit"){
    visitForm.classList.add("hide");
    editForm.classList.add("show");
}

