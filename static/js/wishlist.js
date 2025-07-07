// From wish list add to cart functionality
$(".wish-list__cart-btn").on("click", function() {
  const btn = $(this)
  const index = $(this).attr("data-product-id")

  let quantity = Number($(".product-quantity").val())
  let productID = $(".product-pid-" + index).val()
  let productIMG = $(".product-img-" + index).val()
  let productName = $(".product-title-" + index).val()
  let productPrice = parseFloat($(".product-price-" + index).val().replace(",", "."))
  console.log(productID)
  $.ajax({
    url: "/add-to-cart",
    data: {
      "id": productID,
      "pid": productID,
      "quantity": quantity,
      "title": productName,
      "img": productIMG,
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


// Delete wish list functionality
function deleteWishList(id, count) {
  const wishListCount = document.querySelector(".wish-count");
  
  if(wishListCount.innerText == 1) {
    document.querySelector(".wish-list").innerHTML = `<h2 class="text-center">Список пуст</h2>`
    wishListCount.innerText = "0"
    document.getElementById("wishlist-count").innerText = "0"
  }else {
    document.querySelector(".wishlist-id-"+id).remove();
    wishListCount.innerText = count
    document.getElementById("wishlist-count").innerText = count
  }
}


$(".wish-list__remove").on("click", function() {
  let wishlistID = $(this).attr("data-wishlist-id")
  
  $.ajax({
    url: "/delete_wishlist",
    data: {
      "id": wishlistID
    },
    dataType: "json",
    beforeSend: function() {
      console.log("Deleting")
    },
    success: function(response) {
      console.log(response)
      if(response) {
        deleteWishList(wishlistID, response.count)
      }
    }
  })
})