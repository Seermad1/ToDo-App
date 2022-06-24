const dropDownBtn = document.getElementById("dropdown-btn")
const dropDownMenu = document.getElementById("dropdown-menu")

dropDownBtn.addEventListener("click",()=>{
    dropDownMenu.classList.toggle("show")
})