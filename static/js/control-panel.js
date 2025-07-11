const adminItem = document.querySelectorAll(".admin__item");
adminItem.forEach((item) => {
  item.addEventListener("click", function() {
    document.querySelector(".admin__active-item").classList.remove("admin__active-item");
    item.classList.add("admin__active-item");
  })
})
