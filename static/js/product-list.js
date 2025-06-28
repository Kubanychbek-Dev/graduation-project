// Add to cart functionality
$(".add-to-cart-btn").on("click", function() {
  let btn = $(this)
  let index = btn.attr("data-index")
  let quantity = $(".product-quantity-" + index).val()
  let productID = $(".product-pid-" + index).val()
  let productTitle = $(".product-title-" + index).val()
  let productPrice = $(".current-product-price-" + index).text()
  let productImg = $(".product-img-" + index).val()
  
  // console.log(`${quantity}, ${productID}, ${productTitle}, ${productPrice}` + productImg)
  
  $.ajax({
    url: "/add-to-cart",
    data: {
      "id": productID,
      "quantity": quantity,
      "title": productTitle,
      "img": productImg,
      "price": productPrice,
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

