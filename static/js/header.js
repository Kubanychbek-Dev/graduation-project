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
  
});