// Control panel tabs
const tabs = document.querySelectorAll(".tab");
const adminItem = document.querySelectorAll(".admin__item");

adminItem.forEach((item) => {
  item.addEventListener("click", function() {
    document.querySelector(".admin__active-item").classList.remove("admin__active-item");
    item.classList.add("admin__active-item");

    tabs.forEach((tab) => {
      tab.classList.add("admin-panel--hide");
    })

    const content = document.querySelector("#" + item.dataset.tab);
    content.classList.remove("admin-panel--hide");
  })
})

// Change order status
const orderStatus = document.querySelectorAll("#order-status");
orderStatus.forEach((select) => {
  select.addEventListener("change", function() {
    let status = select.value;
    let dataId = select.getAttribute("data-status");
    
    $.ajax({
      url: "/change_order_status",
      data: {
        "status": status,
        "id": dataId
      },
      dataType: "json",
      beforeSend: function() {
        console.log("Sending")
      },
      success: function(response) {
        console.log(response)
        location.reload(true)
      }
    })
  })
})
