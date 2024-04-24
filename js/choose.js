const btnEmployee = document.querySelector(".type-payment >  .choose #employee");
    const ListEmployee = document.querySelector(".type-payment > #List-employee");
    const btnClient = document.querySelector(".type-payment >  .choose #client");
    const ListClient = document.querySelector(".type-payment > #List-client");

    ListClient.style.display = "flex";
    ListEmployee.style.display = "none";

    // show form list employee 
    if (btnEmployee) {
        btnEmployee.addEventListener("click", function () {
            ListEmployee.style.display = "flex";
            ListClient.style.display = "none";
            btnEmployee.classList.add("btnChoose");
            btnClient.classList.remove("btnChoose");
        });
    }
    // show form list client
    if (btnClient) {
        btnClient.addEventListener("click", function () {
            ListClient.style.display = "flex";
            ListEmployee.style.display = "none";
            btnClient.classList.add("btnChoose");
            btnEmployee.classList.remove("btnChoose");
        });
    }