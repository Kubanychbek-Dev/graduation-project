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
  
});