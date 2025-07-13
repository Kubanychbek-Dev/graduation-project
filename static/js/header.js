window.addEventListener("load", () => {
  function removeAlert() {
    const my_alert = document.querySelector(".alert");

    if (my_alert) {
      setTimeout (() => {
        my_alert.remove();
      }, 3000);
    };
  };
  removeAlert();
  

  const categoryBtn = document.querySelector(".category-btn");
  categoryBtn.addEventListener("click", () => {
    document.querySelector(".category-list").classList.toggle("category-list--show");
  });


  // Header menu--show
const headerToggle = document.querySelector(".header-toggle");
headerToggle.addEventListener("click", function() {
  this.classList.toggle("change");
  document.querySelector(".header-un-menu").classList.toggle("header-un-menu--show");
})
  
});