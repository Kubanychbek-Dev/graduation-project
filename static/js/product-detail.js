// Img turning
const bigImg = document.querySelector(".big-img");
const smallImgs = document.querySelectorAll(".small-img");

const bigImgSrc = bigImg.getAttribute("src").split("/").at(-1);

smallImgs.forEach((img) => {
  if (img.getAttribute("src").split("/").find(src => src === bigImgSrc)) {
    img.classList.add("img--mark");
  }

  img.addEventListener("click", () => {
    const srcData = img.getAttribute("src")
    document.querySelector(".img--mark").classList.remove("img--mark");
    bigImg.setAttribute("src", srcData);
    img.classList.add("img--mark");
  })
});

// Tabs
const tabItem = document.querySelectorAll(".tab__item");
const tabContent = document.querySelectorAll(".tab__content");

tabItem.forEach((item) => {
  item.addEventListener("click", (event) => {
    document.querySelector(".border--bottom").classList.remove("border--bottom");
    item.classList.add("border--bottom");

    const content = document.querySelector("#" + item.dataset.tab);
    
    tabContent.forEach((t) => {
      t.classList.add("tab--hidden");
    })

    content.classList.remove("tab--hidden");

  })
})

// Add Review
const reviewBtn = document.querySelector(".review-btn");
reviewBtn.addEventListener("click", (e) => {
  document.querySelector(".review-form-wrapper").classList.toggle("review-form--show");
})


function addReview(data) {
  const d = new Date()
  const date = d.getDate();
  const month = d.getMonth() + 1;
  const year = d.getFullYear();

  const reviewMenu = document.querySelector(".review-menu");
  const li = document.createElement("li");
  li.classList.add("review-item");
  let stars = "";
  for(let i = 1; i <= data.context.rating; i++) {
    stars += '<i class="fas fa-star text-warning"></i>';
  }
  li.innerHTML = `
  <h5 class="user-name">${data.context.user}</h5>
  <p class="rating-date">
    <span>${date}.${month}.${year}</span> ${stars}
  </p>
  <p class="review-self">${data.context.review}</p>
  `;
  reviewMenu.prepend(li);

  const reviewsCount = document.querySelector("#reviews-count");
  console.log(reviewsCount)
  const intoNum = Number(reviewsCount.textContent) + 1
  reviewsCount.textContent = intoNum;
}


$("#review-form").submit(function (event) {
  event.preventDefault();
  
  $.ajax({
    data: $(this).serialize(),
    method: "POST",
    url: $(this).attr("action"),
    dataType: "json",
    success: function(response) {
      console.log("Data saved...");
      
      if(response.bool == true) {
        $("#review-response").html("Отзыв добавлен");
        $("#average-rating").hide();
        $(".review-form--show").removeClass("review-form--show");

        setInterval(() => {
          $("#review-response").html("");
        }, 3000);

        addReview(response)
      }
    }
  })
})


// Add to cart functionality
$("#add-to-cart-btn").on("click", function() {
  let quantity = $("#product-quantity").val()
  let productID = $("#product-id").val()
  let productPID = $("#product-pid").val()
  let productTitle = $("#product-title").val()
  let productPrice = parseFloat($("#current-product-price").text().replace(",", "."))
  let productImg = $("#product-img").val()
  let btn = $(this)
  
  // console.log(`${quantity}, ${productID}, ${productTitle}, ${productPrice}`)
  $.ajax({
    url: "/add-to-cart",
    data: {
      "id": productID,
      "pid": productPID,
      "quantity": quantity,
      "title": productTitle,
      "price": productPrice,
      "img": productImg
    },
    dataType: "json",
    beforeSend: function() {
      console.log("Adding to cart...");
    },
    success: function(response) {
      btn.html("Добавлено в корзину")
      console.log("Successfully added");
      $("#cart-items-count").text(response.totalcartitems)
    }
  })
})

