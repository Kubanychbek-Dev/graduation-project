// Delete product from cart
function deleteCartItems(item) {
  const itemAmount = document.querySelector("#cart-item-amount").value;
  if(itemAmount == 0) {
    document.querySelector("#cart-container").innerHTML = `
      <h2 class="text-center">Ваша корзина пуста</h2>
    `;
  }else {
    document.getElementById(item.id).remove();
  }
}


$(".delete-cart-product").on("click", function() {
  let productID = $(this).attr("data-product")

  $.ajax({
    url: "/delete_cart_item",
    data: {
      "id": productID
    },
    dataType: "json",
    beforeSend: function() {
      console.log("Deleting...")
    },
    success: function(response) {
      console.log("Success", response.id)
      $(".items-in-cart").text("Товары в корзине: " + response.totalcartitems)
      $("#cart-item-amount").val(response.totalcartitems)
      $("#cart-items-count").text(response.totalcartitems)
      $(".product-amount-span-1").text("Товары("+response.totalcartitems+")")
      $(".product-amount-span-2").text(parseFloat(response.cart_total_amount, 2))
      $(".cart-total-amount-span-1").text(parseFloat(response.cart_total_amount, 2))
      deleteCartItems(response)
    }
  })
})


// Update cart product

$(".update-cart-product").on("click", function() {
  let productID = $(this).attr("data-product")
  let productQTY = $("#product-qty-"+productID).val()
  
  $.ajax({
    url: "/update_cart_item",
    data: {
      "id": productID,
      "quantity": productQTY
    },
    dataType: "json",
    beforeSend: function() {
      console.log("Updating...")
    },
    success: function(response) {
      console.log("Success update", response.id)
      let product = response.data[productID]
      let subtotalPrice = parseFloat(product["price"]) * Number(product["quantity"])

      $(".items-in-cart").text("Товары в корзине: " + response.totalcartitems)
      $("#cart-item-amount").val(response.totalcartitems)
      $("#cart-items-count").text(response.totalcartitems)
      $("#subtotal-price-"+productID).text(Math.round(subtotalPrice))
      $(".product-amount-span-1").text("Товары("+response.totalcartitems+")")
      $(".product-amount-span-2").text(parseFloat(response.cart_total_amount).toFixed(2))
      $(".cart-total-amount-span-1").text(parseFloat(response.cart_total_amount).toFixed(2))
    }
  })
})