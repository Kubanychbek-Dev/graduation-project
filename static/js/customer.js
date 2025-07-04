const greetText = document.querySelector(".profile__greet-text");
userName = greetText.getAttribute("data-username");

const time = new Date();
const hour = time.getHours();

if (hour>=4 && hour<=11) {
   greetText.innerText = `Доброе утро, ${userName}`;
   } else if (hour>=11 && hour<=15) {
      greetText.innerText = `Добрый день, ${userName}`;
      } else if (hour>= 15 && hour<=23) {
        greetText.innerText = `Добрый вечер, ${userName}`;
      } else {
        greetText.innerText = `Спокойной ночи, ${userName}`;
      }


const dashboardItem = document.querySelectorAll(".dashboard__item");
dashboardItem.forEach((item) => {
  item.addEventListener("click", function() {
    document.querySelector(".active-item").classList.remove("active-item");
    item.classList.add("active-item");
  })
})

// Select address
$(".make-default-address").on("click", function() {
  let id = $(this).attr("data-address-id")
  let addressName = $(".address-name-"+id).attr("data-address-name")

  $.ajax({
    url: "/select_address",
    data: {
      "id": id,
      "address": addressName
    },
    dataType: "json",
    success: function(response) {
      console.log("Address selected... ", response.boolean)
      location.reload()
    }
  })
})